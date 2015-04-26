import math
import matplotlib
matplotlib.use("agg")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.backends.backend_pdf import PdfPages 
pdf = PdfPages('outfile.pdf') 

#sns.set(context="paper", font="monospace")
sns.set(context="paper")
#sns.set(context="paper", font_scale=.5)
#sns.set()

#  numjobs | iodepth | read_iops 
fiodata = [
(       1 ,       1 ,     18352),
(       1 ,       2 ,     41528),
(       1 ,       4 ,     86342),
(       1 ,       8 ,    167628),
(       1 ,      16 ,    284939),
(       1 ,      32 ,    325982),
(       1 ,      64 ,    328639),
(       1 ,     128 ,    259234),
(       1 ,     256 ,    328308),
(       1 ,     512 ,    266221),
(       1 ,    1024 ,    311454),
(       1 ,    2048 ,    307397),
(       2 ,       1 ,     42806),
(       2 ,       2 ,     87006),
(       2 ,       4 ,    167914),
(       2 ,       8 ,    307142),
(       2 ,      16 ,    485305),
(       2 ,      32 ,    527752),
(       2 ,      64 ,    535940),
(       2 ,     128 ,    535056),
(       2 ,     256 ,    523688),
(       2 ,     512 ,    544151),
(       2 ,    1024 ,    503716),
(       4 ,       1 ,     83410),
(       4 ,       2 ,    162540),
(       4 ,       4 ,    297679),
(       4 ,       8 ,    494102),
(       4 ,      16 ,    790088),
(       4 ,      32 ,    981115),
(       4 ,      64 ,    937745),
(       4 ,     128 ,    827291),
(       4 ,     256 ,    734552),
(       4 ,     512 ,    966878),
(       8 ,       1 ,    157897),
(       8 ,       2 ,    294023),
(       8 ,       4 ,    513018),
(       8 ,       8 ,    805836),
(       8 ,      16 ,    975725),
(       8 ,      32 ,   1000456),
(       8 ,      64 ,   1002497),
(       8 ,     128 ,   1002905),
(       8 ,     256 ,    997535),
(      16 ,       1 ,    281924),
(      16 ,       2 ,    477645),
(      16 ,       4 ,    808522),
(      16 ,       8 ,    987589),
(      16 ,      16 ,   1001280),
(      16 ,      32 ,   1002019),
(      16 ,      64 ,    990349),
(      16 ,     128 ,    989386),
(      32 ,       1 ,    437690),
(      32 ,       2 ,    581477),
(      32 ,       4 ,    691755),
(      32 ,       8 ,    961569),
(      32 ,      16 ,    974202),
(      32 ,      32 ,    978152),
(      32 ,      64 ,    965226),
(      64 ,       1 ,    486324),
(      64 ,       2 ,    777399),
(      64 ,       4 ,    983578),
(      64 ,       8 ,   1000864),
(      64 ,      16 ,   1000836),
(      64 ,      32 ,    997395),
(     128 ,       1 ,    891782),
(     128 ,       2 ,    997428),
(     128 ,       4 ,   1001181),
(     128 ,       8 ,   1001091),
(     128 ,      16 ,   1000121),
(     256 ,       1 ,    999859),
(     256 ,       2 ,   1002155),
(     256 ,       4 ,   1002339),
(     256 ,       8 ,   1001701),
(     512 ,       1 ,    930063),
(     512 ,       2 ,   1000178),
(     512 ,       4 ,   1000574),
(    1024 ,       1 ,   1982197),
(    1024 ,       2 ,    992985),
(    2048 ,       1 ,   1001428),
]

fiodata = [
(       1 ,       1 ,     94322),
(       1 ,       2 ,    171948),
(       1 ,       4 ,    347958),
(       1 ,       8 ,    359882),
(       1 ,      16 ,    356767),
(       1 ,      32 ,    354846),
(       1 ,      64 ,    365027),
(       1 ,     128 ,    268822),
(       1 ,     256 ,    267973),
(       1 ,     512 ,    267755),
(       1 ,    1024 ,    346422),
(       1 ,    2048 ,    256029),
(       2 ,       1 ,    180885),
(       2 ,       2 ,    307324),
(       2 ,       4 ,    560328),
(       2 ,       8 ,    587587),
(       2 ,      16 ,    554131),
(       2 ,      32 ,    593888),
(       2 ,      64 ,    584018),
(       2 ,     128 ,    599387),
(       2 ,     256 ,    581384),
(       2 ,     512 ,    624826),
(       2 ,    1024 ,    519263),
(       4 ,       1 ,    282609),
(       4 ,       2 ,    485195),
(       4 ,       4 ,    731077),
(       4 ,       8 ,    772753),
(       4 ,      16 ,    795268),
(       4 ,      32 ,    799985),
(       4 ,      64 ,    795733),
(       4 ,     128 ,    708861),
(       4 ,     256 ,    775120),
(       4 ,     512 ,    786552),
(       8 ,       1 ,    374258),
(       8 ,       2 ,    516459),
(       8 ,       4 ,    788354),
(       8 ,       8 ,    800599),
(       8 ,      16 ,    797281),
(       8 ,      32 ,    794830),
(       8 ,      64 ,    799381),
(       8 ,     128 ,    788781),
(       8 ,     256 ,    791217),
(      16 ,       1 ,    511783),
(      16 ,       2 ,    774668),
(      16 ,       4 ,    799963),
(      16 ,       8 ,    797998),
(      16 ,      16 ,    800113),
(      16 ,      32 ,    787551),
(      16 ,      64 ,    800688),
(      16 ,     128 ,    739068),
(      32 ,       1 ,    499097),
(      32 ,       2 ,    759083),
(      32 ,       4 ,    721749),
(      32 ,       8 ,    770760),
(      32 ,      16 ,    787587),
(      32 ,      32 ,    779526),
(      32 ,      64 ,    766722),
(      64 ,       1 ,    647519),
(      64 ,       2 ,    766156),
(      64 ,       4 ,    770139),
(      64 ,       8 ,    776497),
(      64 ,      16 ,    770786),
(      64 ,      32 ,    746461),
(     128 ,       1 ,    800271),
(     128 ,       2 ,    803035),
(     128 ,       4 ,    799044),
(     128 ,       8 ,    795593),
(     128 ,      16 ,    786748),
(     256 ,       1 ,    807286),
(     256 ,       2 ,    805624),
(     256 ,       4 ,    800623),
(     256 ,       8 ,    768156),
(     512 ,       1 ,    806983),
(     512 ,       2 ,    805636),
(     512 ,       4 ,    797635),
(    1024 ,       1 ,    801922),
(    1024 ,       2 ,    806616),
(    2048 ,       1 ,    889158),
]

xticklabels = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
yticklabels = list(reversed(xticklabels))

data = np.ndarray(shape=(12,12), dtype=float, order='F')
data.fill(0)
for d in fiodata:
    numjobs = int(math.log(d[0], 2))
    iodepth = 11- int(math.log(d[1], 2))
    read_iops = d[2]
    data[iodepth][numjobs] = int(read_iops)

#print data

#data = np.random.rand(10,10)
fig_width_cm = 21                         # A4 page
fig_height_cm = 29.7
inches_per_cm = 1 / 2.54              # Convert cm to inches
fig_width = fig_width_cm * inches_per_cm # width in inches
fig_height = fig_height_cm * inches_per_cm       # height in inches
fig_size = [fig_width, fig_height] 

x = np.arange(10)
y = np.arange(10) 

allplots = 3  # This is the variable number of subplots 

fig, axarr = plt.subplots(allplots, 1)
fig.set_size_inches(fig_size) 


#ax.set(xlabel="number of workers", ylabel="IO Depth")
#for plot in range(allplots):
#    axarr[plot].plot(x + plot, y) 

#plt.title('IOPS for random 4kB writes (async. IO): single Intel P3700 NVMe as block device', ax=axarr[0])

for ax in axarr:
    sns.heatmap(data, ax=ax, annot=True, annot_kws={"size": 5}, fmt="g", xticklabels=xticklabels, yticklabels=yticklabels)
#sns.heatmap(data, ax=ax, annot=True, annot_kws={"size": 5}, fmt="g", xticklabels=xticklabels)
#plt.xlabel = xticklabels
#plt.ylabel = yticklabels

#fig.savefig("test3.pdf", figsize=(11.69,8.27))

pdf.savefig()
pdf.close() 

