import os
import sys
import argparse
import math
import matplotlib
matplotlib.use("agg")

import subprocess

import psycopg2

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.backends.backend_pdf import PdfPages 

#sns.set(context="paper", font="monospace")
sns.set(context="paper")
#sns.set(context="paper", font_scale=.5)
#sns.set()


def plot_fio_aio_heatmap(data, ax, cmap=None, vmin=None, vmax=None):
    xticklabels = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    yticklabels = list(reversed(xticklabels))
    heatmap_data = np.ndarray(shape=(12,12), dtype=float, order='F')
    heatmap_data.fill(0)

    ax.set_xlabel('common xlabel')

    for d in data:
        numjobs = int(math.log(d[0], 2))
        iodepth = 11- int(math.log(d[1], 2))
        indicator = d[2]
        heatmap_data[iodepth][numjobs] = round(indicator,1)

    #locs, labels = plt.xticks()
    #plt.setp(labels, rotation=45)
    #ax.set_xlabel('sdfsdf')

    sns.heatmap(heatmap_data, ax=ax, cmap=cmap, vmin=vmin, vmax=vmax, annot=True, annot_kws={"size": 5}, fmt="g", xticklabels=xticklabels, yticklabels=yticklabels)


def create_report_page(report_title, report, data, outfile):

    indicators = report['indicators']
    indicator_headings = report['indicator_headings']

    pdf = PdfPages(outfile) 

    fig_width_cm = 21                         # A4 page
    fig_height_cm = 29.7
    inches_per_cm = 1 / 2.54              # Convert cm to inches
    fig_width = fig_width_cm * inches_per_cm # width in inches
    fig_height = fig_height_cm * inches_per_cm       # height in inches
    fig_size = [fig_width, fig_height] 

    #plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    #plt.tight_layout()


    #fig, ax = plt.subplots()

    #fig.set_size_inches(fig_size)
    #fig.set_label("hello world")
    #ax.set_title('Simple plot')
    #matplotlib.pyplot.text(0,fig_height,"intel p3700")
    from pprint import pprint
    #print pprint(dir(fig))

    allplots = 3  # This is the variable number of subplots 

    fig, axarr = plt.subplots(allplots, 1)
    fig.set_size_inches(fig_size)
    fig.subplots_adjust(hspace=.4)
#    fig.suptitle('{} - {}kB {} (asynchronous IO)'.format(report['name'], report['blocksize'], report['iomode']), fontsize=14)
#    fig.suptitle('{}, {}'.format(report_title, report['title']), fontsize=14)
    fig.suptitle(report_title, fontsize=12)



    #ax.set(xlabel="number of workers", ylabel="IO Depth")
    #for plot in range(allplots):
    #    axarr[plot].plot(x + plot, y) 

    #plt.title('IOPS for random 4kB writes (async. IO): single Intel P3700 NVMe as block device', ax=axarr[0])

    cmap = sns.diverging_palette(h_neg=210, h_pos=350, s=90, l=30, as_cmap=True)
    #cmap2 = sns.blend_palette(["firebrick", "palegreen"], 8) 
    #for ax in axarr:
    axarr[0].set_title(indicator_headings[0])
    plot_fio_aio_heatmap(data[0], axarr[0], cmap=None)
    axarr[0].set_xlabel('number of workers')
    axarr[0].set_ylabel('queue depth')

    axarr[1].set_title(indicator_headings[1])
    plot_fio_aio_heatmap(data[1], axarr[1], cmap="copper_r")
    axarr[1].set_xlabel('number of workers')
    axarr[1].set_ylabel('queue depth')

    axarr[2].set_title(indicator_headings[2])
    plot_fio_aio_heatmap(data[2], axarr[2], cmap="jet", vmin=0, vmax=100)
    axarr[2].set_xlabel('number of workers')
    axarr[2].set_ylabel('queue depth')
    #sns.heatmap(data, ax=ax, annot=True, annot_kws={"size": 5}, fmt="g", xticklabels=xticklabels)
    #plt.xlabel = xticklabels
    #plt.ylabel = yticklabels
    #Spectral, summer, coolwarm, Wistia_r, pink_r, Set1, Set2, Set3,
    # brg_r, Dark2, prism, PuOr_r, afmhot_r, terrain_r, PuBuGn_r, RdPu,
    # gist_ncar_r, gist_yarg_r, Dark2_r, YlGnBu, RdYlBu, hot_r, gist_rainbow_r,
    # gist_stern, PuBu_r, cool_r, cool, gray, copper_r, Greens_r, GnBu, gist_ncar,
    # spring_r, gist_rainbow, gist_heat_r, Wistia, OrRd_r, CMRmap, bone,
    # gist_stern_r, RdYlGn, Pastel2_r, spring, terrain, YlOrRd_r, Set2_r,
    # winter_r, PuBu, RdGy_r, spectral, rainbow, flag_r, jet_r, RdPu_r,
    # gist_yarg, BuGn, Paired_r, hsv_r, bwr, cubehelix, Greens, PRGn,
    # gist_heat, spectral_r, Paired, hsv, Oranges_r, prism_r, Pastel2,
    # Pastel1_r, Pastel1, gray_r, jet, Spectral_r, gnuplot2_r, gist_earth,
    # YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, gnuplot_r, ocean_r, brg,
    # gnuplot2, PuRd_r, bone_r, BuPu, Oranges, RdYlGn_r, PiYG, CMRmap_r, YlGn,
    # binary_r, gist_gray_r, Accent, BuPu_r, gist_gray, flag, bwr_r, RdBu_r, BrBG,
    # Reds, Set1_r, summer_r, GnBu_r, BrBG_r, Reds_r, RdGy, PuRd, Accent_r,
    # Blues, autumn_r, autumn, cubehelix_r, nipy_spectral_r, ocean, PRGn_r,
    # Greys_r, pink, binary, winter, gnuplot, RdYlBu_r, hot, YlOrBr, coolwarm_r,
    # rainbow_r, Purples_r, PiYG_r, YlGn_r, Blues_r, YlOrBr_r, seismic, Purples,
    # seismic_r, RdBu, Greys, BuGn_r, YlOrRd, PuOr, PuBuGn, nipy_spectral, afmhot
    #fig.savefig("test3.pdf", figsize=(11.69,8.27))



    pdf.savefig()
    pdf.close() 
    
    plt.clf()


def get_test_result(conn, test_id, ioengine="aio", blocksize=4, iomode="randread", indicator="read_iops"):

    if indicator == "read_iops":
        sel = "round((result->'jobs'->0->'read'->'iops')::text::float)"

    elif indicator == "read_bw":
        sel = "round((result->'jobs'->0->'read'->'bw')::text::float)"

    elif indicator == "read_latency_q995":
        sel = "round((result->'jobs'->0->'read'->'clat'->'percentile'->'99.500000')::text::float)"

    elif indicator == "write_iops":
        sel = "round((result->'jobs'->0->'write'->'iops')::text::float)"

    elif indicator == "write_bw":
        sel = "round((result->'jobs'->0->'write'->'bw')::text::float)"

    elif indicator == "write_latency_q995":
        sel = "round((result->'jobs'->0->'write'->'clat'->'percentile'->'99.500000')::text::float)"

    elif indicator == "cpu_idle":
        sel = "100. - ((cpu_load->'idle')::text::float)"

    else:
        raise Exception("unknown indicator {}".format(indicator))

    sql = """
        select
            numjobs,
            iodepth,
            {0} as indicator
        from
            perf.tbl_storage_test_result
        where
            test_id = %s
            and ioengine = %s
            and iomode = %s
            and blocksize = %s
    """.format(sel)

    res = []
    cur = conn.cursor()
    cur.execute(sql, (test_id, ioengine, iomode, blocksize))
    for numjobs, iodepth, indicator in cur.fetchall():
        res.append([numjobs, iodepth, indicator])

    return res


def combine_pdf_pages(pages, output, remove=False):
    args = ["pdfunite"]
    args.extend(pages)
    args.append(output)
    subprocess.check_output(args)
    if remove:
        for f in pages:
            os.remove(f)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # target database
    #
    parser.add_argument("--pghost", type=str, default="localhost", help='PostgreSQL database server.')
    parser.add_argument("--pgport", type=int, default=5434, help='PostgreSQL database server listening port.')
    parser.add_argument("--pgdb", type=str, default="adr", help='PostgreSQL database name.')
    parser.add_argument("--pguser", type=str, default="oberstet", help='PostgreSQL database user.')
    parser.add_argument("--pgpassword", type=str, default=os.environ.get('PGPASSWORD', None), help='PostgreSQL database user password.')

    # parse cmd line args
    #
    args = parser.parse_args()

    # connect to DB
    #
    conn = psycopg2.connect(host=args.pghost, port=args.pgport, database=args.pgdb, user=args.pguser, password=args.pgpassword)
    conn.autocommit = True

    reports = []

    # pdfunite nvme_p3700_*.pdf nvme_p3700.pdf

    for name in [
        'nvme_p3700_x1_blockdev',
        'nvme_p3700_x2_raid0_blockdev',
        'nvme_p3700_x4_raid0_blockdev',
        'nvme_p3700_x6_raid0_blockdev',
        'nvme_p3700_x8_raid0_blockdev',
        'nvme_p3700_x2_raid1_blockdev',
        'nvme_p3700_x4_raid10_blockdev',
        'nvme_p3700_x6_raid10_blockdev',
        'nvme_p3700_x8_raid10_blockdev',
    ]:
        l = [
            {
                'name': name,
                'title': "Random Read 4kB",
                'iomode': 'randread',
                'blocksize': 4,
                'indicators': ['read_iops', 'read_latency_q995', 'cpu_idle'],
                'indicator_headings': ['IOPS, reqs/s', r'IO Latency, us (99.5% Quantile)', r'CPU Utilization, %']
            },
            {
                'name': name,
                'title': "Random Write 4kB",
                'iomode': 'randwrite',
                'blocksize': 4,
                'indicators': ['write_iops', 'write_latency_q995', 'cpu_idle'],
                'indicator_headings': ['IOPS, reqs/s', r'IO Latency, us (99.5% Quantile)', r'CPU Utilization, %']
            },

            {
                'name': name,
                'title': "Random Read 8kB",
                'iomode': 'randread',
                'blocksize': 8,
                'indicators': ['read_iops', 'read_latency_q995', 'cpu_idle'],
                'indicator_headings': ['IOPS, reqs/s', r'IO Latency, us (99.5% Quantile)', r'CPU Utilization, %']
            },
            {
                'name': name,
                'title': "Random Write 8kB",
                'iomode': 'randwrite',
                'blocksize': 8,
                'indicators': ['write_iops', 'write_latency_q995', 'cpu_idle'],
                'indicator_headings': ['IOPS, reqs/s', r'IO Latency, us (99.5% Quantile)', r'CPU Utilization, %']
            },
            {
                'name': name,
                'title': "Random Read/Write (70/30) 8kB",
                'iomode': 'randrw',
                'blocksize': 8,
                'indicators': ['write_iops', 'write_latency_q995', 'cpu_idle'],
                'indicator_headings': ['IOPS, reqs/s', r'IO Latency, us (99.5% Quantile)', r'CPU Utilization, %']
            },
            {
                'name': name,
                'title': "Sequential Read 128kB",
                'iomode': 'read',
                'blocksize': 128,
                'indicators': ['read_bw', 'read_latency_q995', 'cpu_idle'],
                'indicator_headings': ['Bandwidth, kB/s', r'IO Latency, us (99.5% Quantile)', r'CPU Utilization, %']
            },
            {
                'name': name,
                'title': "Sequential Write 128kB",
                'iomode': 'write',
                'blocksize': 128,
                'indicators': ['write_bw', 'write_latency_q995', 'cpu_idle'],
                'indicator_headings': ['Bandwidth, kB/s', r'IO Latency, us (99.5% Quantile)', r'CPU Utilization, %']
            },
        ]
        reports.extend(l)

    cnt = 0
    break_at = None

    report_pages = []

    for report in reports:
        if break_at is None or cnt < break_at:
            cur = conn.cursor()
            cur.execute("select id, descr from perf.tbl_storage_test where title = %s", (report['name'],))
            res = cur.fetchone()
            if res is None:
                raise Exception("no such test: '{}'".format(resport['name']))
            test_id, descr = res

            report_title = "{} (Test ID {})\n{}".format(descr, test_id, report['title'])

            data = range(3)
            data[0] = get_test_result(conn, test_id=test_id, indicator=report['indicators'][0], ioengine="aio", blocksize=report['blocksize'], iomode=report['iomode'])
            data[1] = get_test_result(conn, test_id=test_id, indicator=report['indicators'][1], ioengine="aio", blocksize=report['blocksize'], iomode=report['iomode'])
            data[2] = get_test_result(conn, test_id=test_id, indicator=report['indicators'][2], ioengine="aio", blocksize=report['blocksize'], iomode=report['iomode'])

            filename = "{}_aio_{}_{}.pdf".format(report['name'], report['iomode'], report['blocksize'])

            create_report_page(report_title, report, data, filename)

            report_pages.append(filename)

            cnt += 1
        else:
            break

    combine_pdf_pages(report_pages, "brv-sql18-storage-performance.pdf", remove=True)
