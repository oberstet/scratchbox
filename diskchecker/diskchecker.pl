#!/usr/bin/perl
#
# Brad's el-ghetto do-our-storage-stacks-lie?-script
#

sub usage {
    die <<'END';
Usage: diskchecker.pl -s <server[:port]> verify <file>
       diskchecker.pl -s <server[:port]> create <file> <size_in_MB>
       diskchecker.pl -l [port]
END
}

use strict;
use IO::Socket::INET;
use IO::Handle;
use Getopt::Long;
use Socket qw(IPPROTO_TCP TCP_NODELAY);

my $server;
my $listen;
usage() unless GetOptions('server=s' => \$server,
                          'listen:5400' => \$listen);
usage() unless $server || $listen;
usage() if     $server && $listen;

# LISTEN MODE:
listen_mode($listen) if $listen;

# CLIENT MODE:
my $LEN = 16 * 1024;   # 16kB (same as InnoDB page)
my $mode = shift;
usage() unless $mode =~ /^verify|create$/;

my $file = shift or usage();
my $size;
if ($mode eq "create") {
    $size = shift or usage();
}

$server .= ":5400" unless $server =~ /:/;

my $sock = IO::Socket::INET->new(PeerAddr => $server)
    or die "Couldn't connect to host:port of '$server'\n";

setsockopt($sock, IPPROTO_TCP, TCP_NODELAY, pack("l", 1)) or die;

create() if $mode eq "create";
verify() if $mode eq "verify";
exit 0;

sub verify {
    sendmsg($sock, "read");

    my $error_ct = 0;
    my %error_ct;

    my $size = -s $file;
    my $max_pages = int($size / $LEN);

    my $percent;
    my $last_dump = 0;
    my $show_percent = sub {
	printf " verifying: %.02f%%\n", $percent;
    };

    open (F, $file) or die "Couldn't open file $file for read\n";

    while (<$sock>) {
	chomp;
	my ($page, $good, $val, $ago) = split(/\t/, $_);
	$percent = 100 * $page / ($max_pages || 1);

	my $now = time;
	if ($last_dump != $now) {
	    $last_dump = $now;
	    $show_percent->();
	}

	next unless $good;

	my $offset = $page * $LEN;
	sysseek F, $offset, 0;
	my $buf;
	my $rv = sysread(F, $buf, $LEN);
	my $tobe = sprintf("%08x", $val) x ($LEN / 8);
	substr($tobe, $LEN-1, 1) = "\n";

	unless ($buf eq $tobe) {
	    $error_ct{$ago}++;
	    $error_ct++;
	    print "  Error at page $page, $ago seconds before end.\n";
	}
    }
    $show_percent->();

    print "Total errors: $error_ct\n";
    if ($error_ct) {
	print "Histogram of seconds before end:\n";
	foreach (sort { $a <=> $b } keys %error_ct) {
	    printf "  %4d %4d\n", $_, $error_ct{$_};
	}
    }
}

sub create {
    open (F, ">$file") or die "Couldn't open file $file\n";

    my $ioh = IO::Handle->new_from_fd(fileno(F), "w")
	or die;

    my $pages = int( ($size * 1024 * 1024) / $LEN );  # 50 MiB of 16k pages (3200 pages)

    my %page_hit;
    my $pages_hit = 0;
    my $uniq_pages_hit = 0;
    my $start = time();
    my $last_dump = $start;

    while (1) {
	my $rand = int rand 2000000;
	my $buf = sprintf("%08x", $rand) x ($LEN / 8);
	substr($buf, $LEN-1, 1) = "\n";

	my $pagenum = int rand $pages;
	my $offset = $pagenum * $LEN;

        sendmsg($sock, "pre\t$pagenum\t$rand");

        # now wait for acknowledgement
        my $ok = readmsg($sock);
        die "didn't get 'ok' from server ($pagenum $rand), msg=[$ok] = $!" unless $ok eq "ok";

	sysseek F,$offset,0;
	my $wv = syswrite(F, $buf, $LEN);
	die "return value wasn't $LEN\n" unless $wv == $LEN;
	$ioh->sync or die "couldn't do IO::Handle::sync";  # does fsync

	sendmsg($sock, "post\t$pagenum\t$rand");

        $pages_hit++;
        unless ($page_hit{$pagenum}++) {
            $uniq_pages_hit++;
        }

        my $now = time;
        if ($now != $last_dump) {
            $last_dump = $now;
            my $runtime = $now - $start;
            printf("  diskchecker: running %d sec, %.02f%% coverage of %d MB (%d writes; %d/s)\n",
                   $runtime,
                   (100 * $uniq_pages_hit / $pages),
                   $size,
                   $pages_hit,
                   $pages_hit / $runtime,
                   );
        }

    }
}

sub readmsg {
    my $sock = shift;
    my $len;
    my $rv = sysread($sock, $len, 1);
    return undef unless $rv == 1;
    my $msg;
    $rv = sysread($sock, $msg, ord($len));
    return $msg;
}

sub sendmsg {
    my ($sock, $msg) = @_;
    my $rv = syswrite($sock, chr(length($msg)) . $msg);
    my $expect = length($msg) + 1;
    die "sendmsg failed rv=$rv, expect=$expect" unless $rv == $expect;
    return 1;
}

sub listen_mode {
    my $port = shift;
    my $server = IO::Socket::INET->new(ReuseAddr => 1,
                                       Listen => 1,
                                       LocalPort => $port)
        or die "couldn't make server socket\n";

    while (1) {
        print "[server] diskchecker.pl: waiting for connection...\n";
        my $sock = $server->accept()
            or die "  die: no connection?";
        setsockopt($sock, IPPROTO_TCP, TCP_NODELAY, pack("l", 1)) or die;

        fork and next;
        process_incoming_conn($sock);
        exit 0;
    }
}

sub process_incoming_conn {
    my $sock = shift;
    my $peername = getpeername($sock) or
        die "connection not there?\n";
    my ($port, $iaddr) = sockaddr_in($peername);
    my $ip = inet_ntoa($iaddr);

    my $file = "/tmp/$ip.diskchecker";
    die "[$ip] $file is a symlink" if -l $file;

    print "[$ip] New connection\n";

    my $lines = 0;
    my %state;
    my $end;

    while (1) {
        if ($lines) {
            last unless wait_for_readability(fileno($sock), 3);
        }
        my $line = readmsg($sock);
        last unless $line;

        if ($line eq "read") {
            print "[$ip] Sending state info from ${ip}'s last create.\n";
            open (S, "$file") or die "Couldn't open $file for reading.";
            while (<S>) {
                print $sock $_;
            }
            close S;
            print "[$ip] Done.\n";
            exit 0;
        }

        $lines++;
        my $now = time;
        $end = $now;
        my ($state, $pagenum, $rand) = split(/\t/, $line);
        if ($state eq "pre") {
            $state{$pagenum} = [ 0, $rand+0, $now ];
            sendmsg($sock, "ok");
        } elsif ($state eq "post") {
            $state{$pagenum} = [ 1, $rand+0, $now ];
        }
        print "[$ip] $lines writes\n" if $lines % 1000 == 0;
    }

    print "[$ip] Writing state file...\n";
    open (S, ">$file") or die "Couldn't open $file for writing.";
    foreach (sort { $a <=> $b } keys %state) {
        my $v = $state{$_};
        my $before_end = $end - $v->[2];
        print S "$_\t$v->[0]\t$v->[1]\t$before_end\n";
    }
    print "[$ip] Done.\n";
}

sub wait_for_readability {
    my ($fileno, $timeout) = @_;
    return 0 unless $fileno && $timeout;

    my $rin;
    vec($rin, $fileno, 1) = 1;
    my $nfound = select($rin, undef, undef, $timeout);

    return 0 unless defined $nfound;
    return $nfound ? 1 : 0;
}

