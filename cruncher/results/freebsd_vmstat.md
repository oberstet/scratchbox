# nvd7

```console
root@s4l-zfs:~/oberstet # time fio --output fio.log --filename=/dev/nvd7 control4.fio ; vmstat -ia
51.730u 196.999s 4:41.74 88.2%  415+994k 7537842+7597851io 0pf+0w
interrupt                          total       rate
???                                    0          0
irq1:                                  0          0
stray irq1                             0          0
irq0: attimer0                    691089         18
stray irq0                             0          0
irq3: uart1                            0          0
stray irq3                             0          0
irq4: uart0                          186          0
stray irq4                             0          0
irq5:                                  0          0
stray irq5                             0          0
irq6:                                  0          0
stray irq6                             0          0
irq7:                                  0          0
stray irq7                             0          0
irq8: atrtc0                           0          0
stray irq8                             0          0
irq9: acpi0                            2          0
stray irq9                             0          0
irq10:                                 0          0
stray irq10                            0          0
irq11:                                 0          0
stray irq11                            0          0
irq12:                                 0          0
stray irq12                            0          0
irq13:                                 0          0
stray irq13                            0          0
irq14:                                 0          0
stray irq14                            0          0
irq15:                                 0          0
stray irq15                            0          0
irq16:                                 0          0
stray irq16                            0          0
irq17:                                 0          0
stray irq17                            0          0
irq18:                                 0          0
stray irq18                            0          0
irq19:                                 0          0
stray irq19                            0          0
irq20:                                 0          0
stray irq20                            0          0
irq21:                                 0          0
stray irq21                            0          0
irq22:                                 0          0
stray irq22                            0          0
irq23:                                 0          0
stray irq23                            0          0
irq24:                                 0          0
stray irq24                            0          0
irq25:                                 0          0
stray irq25                            0          0
irq26:                                 0          0
stray irq26                            0          0
irq27:                                 0          0
stray irq27                            0          0
irq28:                                 0          0
stray irq28                            0          0
irq29:                                 0          0
stray irq29                            0          0
irq30:                                 0          0
stray irq30                            0          0
irq31:                                 0          0
stray irq31                            0          0
irq32:                                 0          0
stray irq32                            0          0
irq33:                                 0          0
stray irq33                            0          0
irq34:                                 0          0
stray irq34                            0          0
irq35:                                 0          0
stray irq35                            0          0
irq36:                                 0          0
stray irq36                            0          0
irq37:                                 0          0
stray irq37                            0          0
irq38:                                 0          0
stray irq38                            0          0
irq39:                                 0          0
stray irq39                            0          0
irq40:                                 0          0
stray irq40                            0          0
irq41:                                 0          0
stray irq41                            0          0
irq42:                                 0          0
stray irq42                            0          0
irq43:                                 0          0
stray irq43                            0          0
irq44:                                 0          0
stray irq44                            0          0
irq45:                                 0          0
stray irq45                            0          0
irq46:                                 0          0
stray irq46                            0          0
irq47:                                 0          0
stray irq47                            0          0
irq48:                                 0          0
stray irq48                            0          0
irq49:                                 0          0
stray irq49                            0          0
irq50:                                 0          0
stray irq50                            0          0
irq51:                                 0          0
stray irq51                            0          0
irq52:                                 0          0
stray irq52                            0          0
irq53:                                 0          0
stray irq53                            0          0
irq54:                                 0          0
stray irq54                            0          0
irq55:                                 0          0
stray irq55                            0          0
irq56: nvme0                        6440          0
stray irq56                            0          0
irq57:                                 0          0
stray irq57                            0          0
irq58: nvme1                        7270          0
stray irq58                            0          0
irq59:                                 0          0
stray irq59                            0          0
irq60:                                 0          0
stray irq60                            0          0
irq61:                                 0          0
stray irq61                            0          0
irq62:                                 0          0
stray irq62                            0          0
irq63:                                 0          0
stray irq63                            0          0
irq64: nvme2                        7180          0
stray irq64                            0          0
irq65:                                 0          0
stray irq65                            0          0
irq66:                                 0          0
stray irq66                            0          0
irq67:                                 0          0
stray irq67                            0          0
irq68:                                 0          0
stray irq68                            0          0
irq69:                                 0          0
stray irq69                            0          0
irq70:                                 0          0
stray irq70                            0          0
irq71:                                 0          0
stray irq71                            0          0
irq72:                                 0          0
stray irq72                            0          0
irq73:                                 0          0
stray irq73                            0          0
irq74:                                 0          0
stray irq74                            0          0
irq75:                                 0          0
stray irq75                            0          0
irq76:                                 0          0
stray irq76                            0          0
irq77:                                 0          0
stray irq77                            0          0
irq78:                                 0          0
stray irq78                            0          0
irq79:                                 0          0
stray irq79                            0          0
irq80: nvme3                        7163          0
stray irq80                            0          0
irq81:                                 0          0
stray irq81                            0          0
irq82: nvme4                        7149          0
stray irq82                            0          0
irq83:                                 0          0
stray irq83                            0          0
irq84:                                 0          0
stray irq84                            0          0
irq85:                                 0          0
stray irq85                            0          0
irq86:                                 0          0
stray irq86                            0          0
irq87:                                 0          0
stray irq87                            0          0
irq88: nvme5                        6753          0
stray irq88                            0          0
irq89:                                 0          0
stray irq89                            0          0
irq90:                                 0          0
stray irq90                            0          0
irq91:                                 0          0
stray irq91                            0          0
irq92:                                 0          0
stray irq92                            0          0
irq93:                                 0          0
stray irq93                            0          0
irq94:                                 0          0
stray irq94                            0          0
irq95:                                 0          0
stray irq95                            0          0
irq96:                                 0          0
stray irq96                            0          0
irq97:                                 0          0
stray irq97                            0          0
irq98:                                 0          0
stray irq98                            0          0
irq99:                                 0          0
stray irq99                            0          0
irq100:                                0          0
stray irq100                           0          0
irq101:                                0          0
stray irq101                           0          0
irq102:                                0          0
stray irq102                           0          0
irq103:                                0          0
stray irq103                           0          0
irq104: nvme6                       6787          0
stray irq104                           0          0
irq105:                                0          0
stray irq105                           0          0
irq106: nvme7                     145056          3
stray irq106                           0          0
irq107:                                0          0
stray irq107                           0          0
irq108:                                0          0
stray irq108                           0          0
irq109:                                0          0
stray irq109                           0          0
irq110:                                0          0
stray irq110                           0          0
irq111:                                0          0
stray irq111                           0          0
irq112:                                0          0
stray irq112                           0          0
irq113:                                0          0
stray irq113                           0          0
irq114:                                0          0
stray irq114                           0          0
irq115:                                0          0
stray irq115                           0          0
irq116:                                0          0
stray irq116                           0          0
irq117:                                0          0
stray irq117                           0          0
irq118:                                0          0
stray irq118                           0          0
irq119:                                0          0
stray irq119                           0          0
cpu0:timer                       2002387         52
irq256: dmar0:fault                    0          0
stray irq256                           0          0
irq257: dmar0:qi                   22312          0
stray irq257                           0          0
irq258: dmar1:fault                    0          0
stray irq258                           0          0
irq259: dmar1:qi                   22652          0
stray irq259                           0          0
irq260: dmar2:fault                    0          0
stray irq260                           0          0
irq261: dmar2:qi               261874194       6911
stray irq261                           0          0
irq262: dmar3:fault                    0          0
stray irq262                           0          0
irq263: dmar3:qi                  124939          3
stray irq263                           0          0
irq264: hpet0:t0                       0          0
stray irq264                           0          0
irq265: hpet0:t1                       0          0
stray irq265                           0          0
irq266: hpet0:t2                       0          0
stray irq266                           0          0
irq267: hpet0:t3                       0          0
stray irq267                           0          0
irq268: hpet0:t4                       0          0
stray irq268                           0          0
irq269: hpet0:t5                       0          0
stray irq269                           0          0
irq270: hpet0:t6                       0          0
stray irq270                           0          0
irq271: hpet0:t7                       0          0
stray irq271                           0          0
irq272: ix0:que 0                    870          0
stray irq272                           0          0
irq273: ix0:que 1                     36          0
stray irq273                           0          0
irq274: ix0:que 2                      0          0
stray irq274                           0          0
irq275: ix0:que 3                    753          0
stray irq275                           0          0
irq276: ix0:que 4                    219          0
stray irq276                           0          0
irq277: ix0:que 5                  33055          0
stray irq277                           0          0
irq278: ix0:que 6                      8          0
stray irq278                           0          0
irq279: ix0:que 7                   3409          0
stray irq279                           0          0
irq280: ix0:que 8                  20146          0
stray irq280                           0          0
irq281: ix0:que 9                      1          0
stray irq281                           0          0
irq282: ix0:que 10                    19          0
stray irq282                           0          0
irq283: ix0:que 11                    71          0
stray irq283                           0          0
irq284: ix0:que 12                 18516          0
stray irq284                           0          0
irq285: ix0:que 13                  6760          0
stray irq285                           0          0
irq286: ix0:que 14                  3526          0
stray irq286                           0          0
irq287: ix0:que 15                    10          0
stray irq287                           0          0
irq288: ix0:que 16                     2          0
stray irq288                           0          0
irq289: ix0:que 17                     0          0
stray irq289                           0          0
irq290: ix0:que 18                     2          0
stray irq290                           0          0
irq291: ix0:que 19                     2          0
stray irq291                           0          0
irq292: ix0:que 20                     0          0
stray irq292                           0          0
irq293: ix0:que 21                     5          0
stray irq293                           0          0
irq294: ix0:que 22                     0          0
stray irq294                           0          0
irq295: ix0:que 23                     0          0
stray irq295                           0          0
irq296: ix0:que 24                     1          0
stray irq296                           0          0
irq297: ix0:que 25                     3          0
stray irq297                           0          0
irq298: ix0:que 26                     1          0
stray irq298                           0          0
irq299: ix0:que 27                     2          0
stray irq299                           0          0
irq300: ix0:que 28                     5          0
stray irq300                           0          0
irq301: ix0:que 29                     1          0
stray irq301                           0          0
irq302: ix0:que 30                     2          0
stray irq302                           0          0
irq303: ix0:que 31                     1          0
stray irq303                           0          0
irq304: ix0:que 32                     2          0
stray irq304                           0          0
irq305: ix0:que 33                     2          0
stray irq305                           0          0
irq306: ix0:que 34                     3          0
stray irq306                           0          0
irq307: ix0:que 35                     3          0
stray irq307                           0          0
irq308: ix0:que 36                     2          0
stray irq308                           0          0
irq309: ix0:que 37                     1          0
stray irq309                           0          0
irq310: ix0:que 38                     0          0
stray irq310                           0          0
irq311: ix0:que 39                     1          0
stray irq311                           0          0
irq312: ix0:que 40                     1          0
stray irq312                           0          0
irq313: ix0:que 41                     0          0
stray irq313                           0          0
irq314: ix0:que 42                     0          0
stray irq314                           0          0
irq315: ix0:que 43                     0          0
stray irq315                           0          0
irq316: ix0:que 44                     4          0
stray irq316                           0          0
irq317: ix0:que 45                     0          0
stray irq317                           0          0
irq318: ix0:que 46                     1          0
stray irq318                           0          0
irq319: ix0:que 47                     1          0
stray irq319                           0          0
irq320: ix0:link                       2          0
stray irq320                           0          0
irq321: ix1:que 0                      0          0
stray irq321                           0          0
irq322: ix1:que 1                      0          0
stray irq322                           0          0
irq323: ix1:que 2                      0          0
stray irq323                           0          0
irq324: ix1:que 3                      0          0
stray irq324                           0          0
irq325: ix1:que 4                      0          0
stray irq325                           0          0
irq326: ix1:que 5                      0          0
stray irq326                           0          0
irq327: ix1:que 6                      0          0
stray irq327                           0          0
irq328: ix1:que 7                      0          0
stray irq328                           0          0
irq329: ix1:que 8                      0          0
stray irq329                           0          0
irq330: ix1:que 9                      0          0
stray irq330                           0          0
irq331: ix1:que 10                     0          0
stray irq331                           0          0
irq332: ix1:que 11                     0          0
stray irq332                           0          0
irq333: ix1:que 12                     0          0
stray irq333                           0          0
irq334: ix1:que 13                     0          0
stray irq334                           0          0
irq335: ix1:que 14                     0          0
stray irq335                           0          0
irq336: ix1:que 15                     0          0
stray irq336                           0          0
irq337: ix1:que 16                     0          0
stray irq337                           0          0
irq338: ix1:que 17                     0          0
stray irq338                           0          0
irq339: ix1:que 18                     0          0
stray irq339                           0          0
irq340: ix1:que 19                     0          0
stray irq340                           0          0
irq341: ix1:que 20                     0          0
stray irq341                           0          0
irq342: ix1:que 21                     0          0
stray irq342                           0          0
irq343: ix1:que 22                     0          0
stray irq343                           0          0
irq344: ix1:que 23                     0          0
stray irq344                           0          0
irq345: ix1:que 24                     0          0
stray irq345                           0          0
irq346: ix1:que 25                     0          0
stray irq346                           0          0
irq347: ix1:que 26                     0          0
stray irq347                           0          0
irq348: ix1:que 27                     0          0
stray irq348                           0          0
irq349: ix1:que 28                     0          0
stray irq349                           0          0
irq350: ix1:que 29                     0          0
stray irq350                           0          0
irq351: ix1:que 30                     0          0
stray irq351                           0          0
irq352: ix1:que 31                     0          0
stray irq352                           0          0
irq353: ix1:que 32                     0          0
stray irq353                           0          0
irq354: ix1:que 33                     0          0
stray irq354                           0          0
irq355: ix1:que 34                     0          0
stray irq355                           0          0
irq356: ix1:que 35                     0          0
stray irq356                           0          0
irq357: ix1:que 36                     0          0
stray irq357                           0          0
irq358: ix1:que 37                     0          0
stray irq358                           0          0
irq359: ix1:que 38                     0          0
stray irq359                           0          0
irq360: ix1:que 39                     0          0
stray irq360                           0          0
irq361: ix1:que 40                     0          0
stray irq361                           0          0
irq362: ix1:que 41                     0          0
stray irq362                           0          0
irq363: ix1:que 42                     0          0
stray irq363                           0          0
irq364: ix1:que 43                     0          0
stray irq364                           0          0
irq365: ix1:que 44                     0          0
stray irq365                           0          0
irq366: ix1:que 45                     0          0
stray irq366                           0          0
irq367: ix1:que 46                     0          0
stray irq367                           0          0
irq368: ix1:que 47                     0          0
stray irq368                           0          0
irq369: ix1:link                       0          0
stray irq369                           0          0
irq370: mpr0                       38577          1
stray irq370                           0          0
irq371: mpr1                    70677891       1865
stray irq371                           0          0
cpu33:timer                      1552683         40
cpu7:timer                       1406283         37
cpu2:timer                       1552200         40
cpu1:timer                       1617460         42
cpu28:timer                      1704814         44
cpu9:timer                       1416612         37
cpu11:timer                      3723935         98
cpu42:timer                      1672214         44
cpu10:timer                      1372377         36
cpu8:timer                       1361434         35
cpu6:timer                       1532354         40
cpu4:timer                       2279817         60
cpu5:timer                       1739532         45
cpu47:timer                      2393384         63
cpu3:timer                       1510744         39
cpu34:timer                      1563040         41
cpu22:timer                       917837         24
cpu45:timer                      1603259         42
cpu12:timer                       880207         23
cpu37:timer                      1727940         45
cpu24:timer                      1685277         44
cpu27:timer                      1602982         42
cpu39:timer                      1868810         49
cpu38:timer                      1805502         47
cpu40:timer                      1697140         44
cpu25:timer                      1659572         43
cpu44:timer                      1678948         44
cpu43:timer                      1708491         45
cpu41:timer                      1725079         45
cpu36:timer                      1827148         48
cpu20:timer                       877593         23
cpu46:timer                      1809901         47
cpu16:timer                      1290950         34
cpu26:timer                      1589507         41
cpu29:timer                      1645801         43
cpu32:timer                      1561514         41
cpu18:timer                      1004460         26
cpu35:timer                      1569212         41
cpu31:timer                      1639349         43
cpu30:timer                      1603249         42
cpu15:timer                      1220436         32
cpu19:timer                       831759         21
cpu23:timer                      3470358         91
cpu17:timer                      6858334        181
cpu13:timer                       941171         24
cpu14:timer                       971374         25
cpu21:timer                      1523312         40
Total                          416930831      11003
```

# nvd0

```console
root@s4l-zfs:~/oberstet # time fio --output fio.log --filename=/dev/nvd0 control4.fio ; vmstat -ia
43.992u 141.736s 4:41.83 65.8%  413+989k 7686733+7544085io 0pf+0w
interrupt                          total       rate
???                                    0          0
irq1:                                  0          0
stray irq1                             0          0
irq0: attimer0                    699000         18
stray irq0                             0          0
irq3: uart1                            0          0
stray irq3                             0          0
irq4: uart0                          186          0
stray irq4                             0          0
irq5:                                  0          0
stray irq5                             0          0
irq6:                                  0          0
stray irq6                             0          0
irq7:                                  0          0
stray irq7                             0          0
irq8: atrtc0                           0          0
stray irq8                             0          0
irq9: acpi0                            2          0
stray irq9                             0          0
irq10:                                 0          0
stray irq10                            0          0
irq11:                                 0          0
stray irq11                            0          0
irq12:                                 0          0
stray irq12                            0          0
irq13:                                 0          0
stray irq13                            0          0
irq14:                                 0          0
stray irq14                            0          0
irq15:                                 0          0
stray irq15                            0          0
irq16:                                 0          0
stray irq16                            0          0
irq17:                                 0          0
stray irq17                            0          0
irq18:                                 0          0
stray irq18                            0          0
irq19:                                 0          0
stray irq19                            0          0
irq20:                                 0          0
stray irq20                            0          0
irq21:                                 0          0
stray irq21                            0          0
irq22:                                 0          0
stray irq22                            0          0
irq23:                                 0          0
stray irq23                            0          0
irq24:                                 0          0
stray irq24                            0          0
irq25:                                 0          0
stray irq25                            0          0
irq26:                                 0          0
stray irq26                            0          0
irq27:                                 0          0
stray irq27                            0          0
irq28:                                 0          0
stray irq28                            0          0
irq29:                                 0          0
stray irq29                            0          0
irq30:                                 0          0
stray irq30                            0          0
irq31:                                 0          0
stray irq31                            0          0
irq32:                                 0          0
stray irq32                            0          0
irq33:                                 0          0
stray irq33                            0          0
irq34:                                 0          0
stray irq34                            0          0
irq35:                                 0          0
stray irq35                            0          0
irq36:                                 0          0
stray irq36                            0          0
irq37:                                 0          0
stray irq37                            0          0
irq38:                                 0          0
stray irq38                            0          0
irq39:                                 0          0
stray irq39                            0          0
irq40:                                 0          0
stray irq40                            0          0
irq41:                                 0          0
stray irq41                            0          0
irq42:                                 0          0
stray irq42                            0          0
irq43:                                 0          0
stray irq43                            0          0
irq44:                                 0          0
stray irq44                            0          0
irq45:                                 0          0
stray irq45                            0          0
irq46:                                 0          0
stray irq46                            0          0
irq47:                                 0          0
stray irq47                            0          0
irq48:                                 0          0
stray irq48                            0          0
irq49:                                 0          0
stray irq49                            0          0
irq50:                                 0          0
stray irq50                            0          0
irq51:                                 0          0
stray irq51                            0          0
irq52:                                 0          0
stray irq52                            0          0
irq53:                                 0          0
stray irq53                            0          0
irq54:                                 0          0
stray irq54                            0          0
irq55:                                 0          0
stray irq55                            0          0
irq56: nvme0                        9233          0
stray irq56                            0          0
irq57:                                 0          0
stray irq57                            0          0
irq58: nvme1                        7270          0
stray irq58                            0          0
irq59:                                 0          0
stray irq59                            0          0
irq60:                                 0          0
stray irq60                            0          0
irq61:                                 0          0
stray irq61                            0          0
irq62:                                 0          0
stray irq62                            0          0
irq63:                                 0          0
stray irq63                            0          0
irq64: nvme2                        7180          0
stray irq64                            0          0
irq65:                                 0          0
stray irq65                            0          0
irq66:                                 0          0
stray irq66                            0          0
irq67:                                 0          0
stray irq67                            0          0
irq68:                                 0          0
stray irq68                            0          0
irq69:                                 0          0
stray irq69                            0          0
irq70:                                 0          0
stray irq70                            0          0
irq71:                                 0          0
stray irq71                            0          0
irq72:                                 0          0
stray irq72                            0          0
irq73:                                 0          0
stray irq73                            0          0
irq74:                                 0          0
stray irq74                            0          0
irq75:                                 0          0
stray irq75                            0          0
irq76:                                 0          0
stray irq76                            0          0
irq77:                                 0          0
stray irq77                            0          0
irq78:                                 0          0
stray irq78                            0          0
irq79:                                 0          0
stray irq79                            0          0
irq80: nvme3                        7163          0
stray irq80                            0          0
irq81:                                 0          0
stray irq81                            0          0
irq82: nvme4                        7149          0
stray irq82                            0          0
irq83:                                 0          0
stray irq83                            0          0
irq84:                                 0          0
stray irq84                            0          0
irq85:                                 0          0
stray irq85                            0          0
irq86:                                 0          0
stray irq86                            0          0
irq87:                                 0          0
stray irq87                            0          0
irq88: nvme5                        6753          0
stray irq88                            0          0
irq89:                                 0          0
stray irq89                            0          0
irq90:                                 0          0
stray irq90                            0          0
irq91:                                 0          0
stray irq91                            0          0
irq92:                                 0          0
stray irq92                            0          0
irq93:                                 0          0
stray irq93                            0          0
irq94:                                 0          0
stray irq94                            0          0
irq95:                                 0          0
stray irq95                            0          0
irq96:                                 0          0
stray irq96                            0          0
irq97:                                 0          0
stray irq97                            0          0
irq98:                                 0          0
stray irq98                            0          0
irq99:                                 0          0
stray irq99                            0          0
irq100:                                0          0
stray irq100                           0          0
irq101:                                0          0
stray irq101                           0          0
irq102:                                0          0
stray irq102                           0          0
irq103:                                0          0
stray irq103                           0          0
irq104: nvme6                       6787          0
stray irq104                           0          0
irq105:                                0          0
stray irq105                           0          0
irq106: nvme7                     145056          3
stray irq106                           0          0
irq107:                                0          0
stray irq107                           0          0
irq108:                                0          0
stray irq108                           0          0
irq109:                                0          0
stray irq109                           0          0
irq110:                                0          0
stray irq110                           0          0
irq111:                                0          0
stray irq111                           0          0
irq112:                                0          0
stray irq112                           0          0
irq113:                                0          0
stray irq113                           0          0
irq114:                                0          0
stray irq114                           0          0
irq115:                                0          0
stray irq115                           0          0
irq116:                                0          0
stray irq116                           0          0
irq117:                                0          0
stray irq117                           0          0
irq118:                                0          0
stray irq118                           0          0
irq119:                                0          0
stray irq119                           0          0
cpu0:timer                       2094234         54
irq256: dmar0:fault                    0          0
stray irq256                           0          0
irq257: dmar0:qi                15232841        397
stray irq257                           0          0
irq258: dmar1:fault                    0          0
stray irq258                           0          0
irq259: dmar1:qi                   22652          0
stray irq259                           0          0
irq260: dmar2:fault                    0          0
stray irq260                           0          0
irq261: dmar2:qi               261874208       6832
stray irq261                           0          0
irq262: dmar3:fault                    0          0
stray irq262                           0          0
irq263: dmar3:qi                  125499          3
stray irq263                           0          0
irq264: hpet0:t0                       0          0
stray irq264                           0          0
irq265: hpet0:t1                       0          0
stray irq265                           0          0
irq266: hpet0:t2                       0          0
stray irq266                           0          0
irq267: hpet0:t3                       0          0
stray irq267                           0          0
irq268: hpet0:t4                       0          0
stray irq268                           0          0
irq269: hpet0:t5                       0          0
stray irq269                           0          0
irq270: hpet0:t6                       0          0
stray irq270                           0          0
irq271: hpet0:t7                       0          0
stray irq271                           0          0
irq272: ix0:que 0                    884          0
stray irq272                           0          0
irq273: ix0:que 1                     36          0
stray irq273                           0          0
irq274: ix0:que 2                      0          0
stray irq274                           0          0
irq275: ix0:que 3                    753          0
stray irq275                           0          0
irq276: ix0:que 4                    219          0
stray irq276                           0          0
irq277: ix0:que 5                  33055          0
stray irq277                           0          0
irq278: ix0:que 6                      8          0
stray irq278                           0          0
irq279: ix0:que 7                   3520          0
stray irq279                           0          0
irq280: ix0:que 8                  20149          0
stray irq280                           0          0
irq281: ix0:que 9                      1          0
stray irq281                           0          0
irq282: ix0:que 10                    19          0
stray irq282                           0          0
irq283: ix0:que 11                    71          0
stray irq283                           0          0
irq284: ix0:que 12                 18516          0
stray irq284                           0          0
irq285: ix0:que 13                  6760          0
stray irq285                           0          0
irq286: ix0:que 14                  3614          0
stray irq286                           0          0
irq287: ix0:que 15                    10          0
stray irq287                           0          0
irq288: ix0:que 16                     2          0
stray irq288                           0          0
irq289: ix0:que 17                     0          0
stray irq289                           0          0
irq290: ix0:que 18                     2          0
stray irq290                           0          0
irq291: ix0:que 19                     2          0
stray irq291                           0          0
irq292: ix0:que 20                     0          0
stray irq292                           0          0
irq293: ix0:que 21                     5          0
stray irq293                           0          0
irq294: ix0:que 22                     0          0
stray irq294                           0          0
irq295: ix0:que 23                     0          0
stray irq295                           0          0
irq296: ix0:que 24                     1          0
stray irq296                           0          0
irq297: ix0:que 25                     3          0
stray irq297                           0          0
irq298: ix0:que 26                     1          0
stray irq298                           0          0
irq299: ix0:que 27                     2          0
stray irq299                           0          0
irq300: ix0:que 28                     5          0
stray irq300                           0          0
irq301: ix0:que 29                     1          0
stray irq301                           0          0
irq302: ix0:que 30                     2          0
stray irq302                           0          0
irq303: ix0:que 31                     1          0
stray irq303                           0          0
irq304: ix0:que 32                     2          0
stray irq304                           0          0
irq305: ix0:que 33                     3          0
stray irq305                           0          0
irq306: ix0:que 34                     3          0
stray irq306                           0          0
irq307: ix0:que 35                     3          0
stray irq307                           0          0
irq308: ix0:que 36                     2          0
stray irq308                           0          0
irq309: ix0:que 37                     1          0
stray irq309                           0          0
irq310: ix0:que 38                     0          0
stray irq310                           0          0
irq311: ix0:que 39                     1          0
stray irq311                           0          0
irq312: ix0:que 40                     1          0
stray irq312                           0          0
irq313: ix0:que 41                     0          0
stray irq313                           0          0
irq314: ix0:que 42                     0          0
stray irq314                           0          0
irq315: ix0:que 43                     0          0
stray irq315                           0          0
irq316: ix0:que 44                     4          0
stray irq316                           0          0
irq317: ix0:que 45                     0          0
stray irq317                           0          0
irq318: ix0:que 46                     1          0
stray irq318                           0          0
irq319: ix0:que 47                     1          0
stray irq319                           0          0
irq320: ix0:link                       2          0
stray irq320                           0          0
irq321: ix1:que 0                      0          0
stray irq321                           0          0
irq322: ix1:que 1                      0          0
stray irq322                           0          0
irq323: ix1:que 2                      0          0
stray irq323                           0          0
irq324: ix1:que 3                      0          0
stray irq324                           0          0
irq325: ix1:que 4                      0          0
stray irq325                           0          0
irq326: ix1:que 5                      0          0
stray irq326                           0          0
irq327: ix1:que 6                      0          0
stray irq327                           0          0
irq328: ix1:que 7                      0          0
stray irq328                           0          0
irq329: ix1:que 8                      0          0
stray irq329                           0          0
irq330: ix1:que 9                      0          0
stray irq330                           0          0
irq331: ix1:que 10                     0          0
stray irq331                           0          0
irq332: ix1:que 11                     0          0
stray irq332                           0          0
irq333: ix1:que 12                     0          0
stray irq333                           0          0
irq334: ix1:que 13                     0          0
stray irq334                           0          0
irq335: ix1:que 14                     0          0
stray irq335                           0          0
irq336: ix1:que 15                     0          0
stray irq336                           0          0
irq337: ix1:que 16                     0          0
stray irq337                           0          0
irq338: ix1:que 17                     0          0
stray irq338                           0          0
irq339: ix1:que 18                     0          0
stray irq339                           0          0
irq340: ix1:que 19                     0          0
stray irq340                           0          0
irq341: ix1:que 20                     0          0
stray irq341                           0          0
irq342: ix1:que 21                     0          0
stray irq342                           0          0
irq343: ix1:que 22                     0          0
stray irq343                           0          0
irq344: ix1:que 23                     0          0
stray irq344                           0          0
irq345: ix1:que 24                     0          0
stray irq345                           0          0
irq346: ix1:que 25                     0          0
stray irq346                           0          0
irq347: ix1:que 26                     0          0
stray irq347                           0          0
irq348: ix1:que 27                     0          0
stray irq348                           0          0
irq349: ix1:que 28                     0          0
stray irq349                           0          0
irq350: ix1:que 29                     0          0
stray irq350                           0          0
irq351: ix1:que 30                     0          0
stray irq351                           0          0
irq352: ix1:que 31                     0          0
stray irq352                           0          0
irq353: ix1:que 32                     0          0
stray irq353                           0          0
irq354: ix1:que 33                     0          0
stray irq354                           0          0
irq355: ix1:que 34                     0          0
stray irq355                           0          0
irq356: ix1:que 35                     0          0
stray irq356                           0          0
irq357: ix1:que 36                     0          0
stray irq357                           0          0
irq358: ix1:que 37                     0          0
stray irq358                           0          0
irq359: ix1:que 38                     0          0
stray irq359                           0          0
irq360: ix1:que 39                     0          0
stray irq360                           0          0
irq361: ix1:que 40                     0          0
stray irq361                           0          0
irq362: ix1:que 41                     0          0
stray irq362                           0          0
irq363: ix1:que 42                     0          0
stray irq363                           0          0
irq364: ix1:que 43                     0          0
stray irq364                           0          0
irq365: ix1:que 44                     0          0
stray irq365                           0          0
irq366: ix1:que 45                     0          0
stray irq366                           0          0
irq367: ix1:que 46                     0          0
stray irq367                           0          0
irq368: ix1:que 47                     0          0
stray irq368                           0          0
irq369: ix1:link                       0          0
stray irq369                           0          0
irq370: mpr0                       39053          1
stray irq370                           0          0
irq371: mpr1                    70677905       1844
stray irq371                           0          0
cpu33:timer                      1644347         42
cpu7:timer                       1496596         39
cpu2:timer                       1650180         43
cpu1:timer                       1704000         44
cpu28:timer                      1779910         46
cpu9:timer                       1501598         39
cpu11:timer                      3822358         99
cpu42:timer                      1763149         46
cpu10:timer                      1450967         37
cpu8:timer                       1453276         37
cpu6:timer                       1626029         42
cpu4:timer                       2590682         67
cpu5:timer                       1843544         48
cpu47:timer                      2474297         64
cpu3:timer                       1594442         41
cpu34:timer                      1622317         42
cpu22:timer                       946412         24
cpu45:timer                      1686979         44
cpu12:timer                       907952         23
cpu37:timer                      1830737         47
cpu24:timer                      1767891         46
cpu27:timer                      1691795         44
cpu39:timer                      1962154         51
cpu38:timer                      1887112         49
cpu40:timer                      1792775         46
cpu25:timer                      1723007         44
cpu44:timer                      1768656         46
cpu43:timer                      1794691         46
cpu41:timer                      1808993         47
cpu36:timer                      1959877         51
cpu20:timer                       905078         23
cpu46:timer                      1888045         49
cpu16:timer                      1312523         34
cpu26:timer                      1657578         43
cpu29:timer                      1705837         44
cpu32:timer                      1622960         42
cpu18:timer                      1029192         26
cpu35:timer                      1628286         42
cpu31:timer                      1768386         46
cpu30:timer                      1674082         43
cpu15:timer                      1248990         32
cpu19:timer                       861440         22
cpu23:timer                      3492943         91
cpu17:timer                      6883352        179
cpu13:timer                      1254544         32
cpu14:timer                       997250         26
cpu21:timer                      1550387         40
Total                          436077433      11378
```
