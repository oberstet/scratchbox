#include <dtrace.h>
#include <signal.h>
#include <stdio.h>

static dtrace_hdl_t* g_dtp;

static int chewrec (const dtrace_probedata_t *data, const dtrace_recdesc_t *rec, void *arg) {
   printf("chewing dtrace record ..\n");
   // A NULL rec indicates that we've processed the last record.
   if (rec == NULL) {
      return (DTRACE_CONSUME_NEXT);
   }
   return (DTRACE_CONSUME_THIS);
}

static const char* g_prog = "BEGIN { printf(\"hello from dtrace\\n\"); }";
//static const char* g_prog = "syscall::open*:entry { printf(\"%s %s\\n\", execname, copyinstr(arg0)); }";

static int g_intr;
static int g_exited;

static void intr (int signo) {
   g_intr = 1;
}


int main (int argc, char** argv) {
   int err;

   if ((g_dtp = dtrace_open(DTRACE_VERSION, 0, &err)) == NULL) {
      fprintf(stderr, "failed to initialize dtrace: %s\n", dtrace_errmsg(NULL, err));
      return -1;
   }
   printf("Dtrace initialized\n");

   (void) dtrace_setopt(g_dtp, "bufsize", "4m");
   (void) dtrace_setopt(g_dtp, "aggsize", "4m");
   printf("dtrace options set\n");

   dtrace_prog_t* prog;
   if ((prog = dtrace_program_strcompile(g_dtp, g_prog, DTRACE_PROBESPEC_NAME, 0, 0, NULL)) == NULL) {
      fprintf(stderr, "failed to compile dtrace program\n");
      return -1;
   } else {
      printf("dtrace program compiled\n");
   }

   dtrace_proginfo_t info;
   if (dtrace_program_exec(g_dtp, prog, &info) == -1) {
      fprintf(stderr, "failed to enable dtrace probes\n");
      return -1;
   } else {
      printf("dtrace probes enabled\n");
   }

   struct sigaction act;
   (void) sigemptyset(&act.sa_mask);
   act.sa_flags = 0;
   act.sa_handler = intr;
   (void) sigaction(SIGINT, &act, NULL);
   (void) sigaction(SIGTERM, &act, NULL);

   if (dtrace_go(g_dtp) != 0) {
      fprintf(stderr, "could not start instrumentation\n");
      return -1;
   } else {
      printf("instrumentation started ..\n");
   } 

   int done = 0;
   do {
      if (!g_intr && !done) {
         dtrace_sleep(g_dtp);
      }

      if (done || g_intr || g_exited) {
         done = 1;
         if (dtrace_stop(g_dtp) == -1) {
            fprintf(stderr, "could not stop tracing\n");
            return -1;
         }
      }

      switch (dtrace_work(g_dtp, stdout, NULL, chewrec, NULL)) {
         case DTRACE_WORKSTATUS_DONE:
            done = 1;
            break;
         case DTRACE_WORKSTATUS_OKAY:
            break;
         default:
            fprintf(stderr, "processing aborted");
            return -1;
      }
   } while (!done);

   printf("closing dtrace\n");
   dtrace_close(g_dtp);

   return 0;
}

