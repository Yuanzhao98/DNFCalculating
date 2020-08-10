from PublicReference.base import *

黑曜神等级 = 100 + 5

class 黑曜神技能0(主动技能):
    名称 = '魔灵召唤：波拉斯'
    备注 = '(每秒DPS)'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 444.15
    成长 = 13.94
    攻击次数 = 12/4/20
    #数据1 = [0, 319, 362, 380, 397, 417, 435, 452, 470, 490, 509, 526, 546, 565, 583, 603, 622, 640, 658, 675, 694, 714, 733, 751, 770, 790, 806, 825, 845, 862, 880, 901, 919, 936, 956, 974, 993, 1011, 1031, 1050, 1065, 1086, 1104,  1122, 1142, 1161, 1179, 1199, 1216, 1235, 1254, 1272, 1290, 1309, 1327, 1346, 1366, 1384, 1403, 1422, 1440, 1458, 1477, 1495, 1514, 1532, 1550, 1571, 1590, 1608, 1626]
    #攻击次数1 = 10
    #数据2 = [0, 1277, 1445, 1518, 1586, 1666, 1741, 1808, 1882, 1962, 2036, 2103, 2184, 2258, 2332, 2413, 2486, 2560, 2634, 2702, 2775, 2856, 2930, 3004, 3078, 3158, 3226, 3299, 3380, 3447, 3522, 3602, 3676, 3743, 3824, 3898, 3971, 4046, 4126, 4200, 4261, 4341, 4415, 4489, 4570, 4643, 4718, 4798, 4866, 4939, 5013, 5087, 5161, 5235, 5309, 5382, 5463, 5538, 5611, 5685, 5759, 5833, 5907, 5981, 6054, 6129, 6202, 6283, 6357, 6431, 6505]
    #攻击次数2 = 2
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型):
        return 1.0

class 黑曜神技能1(主动技能):
    名称 = '魔灵召唤：瓦尔琪'
    备注 = '(每秒DPS)'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 328.09
    成长 = 14.5
    攻击次数 = 14/7/20
    #数据1 = [0, 177, 218, 235, 254, 273, 292, 310, 328, 347, 366, 384, 403, 422, 440, 458, 477, 496, 514, 533, 553, 570,  588, 608, 626, 644, 664, 682, 701, 719, 738, 757, 775, 794, 812, 830, 850, 868, 887, 905, 924, 943, 961, 979, 998, 1017, 1034, 1054, 1072, 1092, 1110, 1128, 1147, 1166, 1184, 1203, 1221, 1240, 1258, 1277, 1295, 1314, 1333, 1352, 1370, 1389, 1407, 1425, 1445, 1463, 1482]
    #攻击次数1 = 11
    #数据2 = [0, 511, 558, 607, 655, 702, 750, 797, 846, 894, 942, 990, 1037, 1085, 1133, 1182, 1231, 1278, 1326, 1374, 1421, 1471, 1518, 1566, 1612, 1660, 1708, 1757, 1805, 1852, 1901, 1947, 1996, 2044, 2092, 2139, 2187, 2235, 2284, 2332, 2380, 2427, 2475, 2523, 2572, 2621, 2668, 2714, 2763, 2810, 2859, 2906, 2955, 3002, 3050, 3097,  3147, 3194, 3242, 3290, 3337, 3386, 3434, 3482, 3529, 3577, 3626, 3674, 3720, 3768, 3816]
    #攻击次数2 = 3
    TP成长 = 0.10
    TP上限 = 5
    def 等效CD(self, 武器类型):
        return 1.0

class 黑曜神技能2(被动技能):
    名称 = '魔灵血统'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

class 黑曜神技能3(被动技能):
    名称 = '力量法则'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['军团列阵','魔幻旋风','毁灭突进','翔空剑','聚灵升空剑','魔神百裂拳','黑暗冲击','午夜嘉年华','绚丽耀光','魔灵乱舞','黑曜之眸：亚丁降临']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.085 + 0.015 * self.等级, 5)

class 黑曜神技能4(主动技能):
    名称 = '魔灵召唤：狂暴布洛克'
    备注 = '(每秒DPS)'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 506.41
    成长 = 22.14
    攻击次数 = 14/5.5/20
    #数据1 = [0, 724, 789, 859, 926, 994, 1061, 1129, 1196, 1263, 1331, 1399, 1466, 1533, 1600, 1671, 1740, 1807, 1875, 1941, 2009, 2078, 2147, 2214, 2279, 2346, 2415, 2484, 2552, 2619, 2686, 2753, 2823, 2890, 2957, 3025, 3093, 3160, 3227, 3295, 3362, 3430, 3497, 3565, 3636, 3704, 3771, 3838, 3904, 3972, 4041, 4109, 4176, 4244, 4311, 4379, 4448, 4515, 4583, 4650, 4718, 4786, 4855, 4922, 4990, 5057, 5124, 5192, 5260, 5327, 5394]
    #攻击次数1 = 3
    #数据2 = [0, 651, 711, 773, 833, 895, 955, 1015, 1076, 1137, 1198, 1258, 1319, 1380, 1441, 1505, 1565, 1626, 1687, 1747, 1808, 1871, 1931, 1993, 2051, 2112, 2173, 2236, 2297, 2357, 2417, 2479, 2541, 2601, 2662, 2723, 2784,  2844, 2904, 2966, 3027, 3088, 3148, 3209, 3272, 3333, 3394, 3453, 3514, 3575, 3637, 3698, 3758, 3819, 3880, 3940, 4003, 4064, 4124, 4185, 4246, 4308, 4369, 4430, 4491, 4551, 4612, 4673, 4733, 4793, 4855]
    #攻击次数2 = 3
    #数据3 = [0, 203, 221, 240, 259, 278, 297, 316, 335, 355, 373, 392, 410, 429, 448, 468, 487, 507, 525, 544, 563, 582, 600, 620, 638, 657, 676, 696, 715, 733, 752, 771, 790, 809, 828, 847, 866, 885, 905, 923, 941, 960, 979, 998, 1018, 1037, 1056, 1074, 1094, 1112, 1131, 1150, 1169, 1188, 1207, 1226, 1246, 1265, 1283, 1302, 1321, 1340, 1359, 1378, 1397, 1416, 1436, 1454, 1472, 1492, 1510]
    #攻击次数3 = 8
    #出血数据4 = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,10, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 13, 13, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 19, 19, 20, 20,20, 21, 21, 21, 22, 22, 24, 24, 25, 25, 25, 26, 26, 26, 27, 27, 27]
    TP成长 = 0.10
    TP上限 = 5
    def 等效CD(self, 武器类型):
        return 1.0
        
class 黑曜神技能5(主动技能):
    名称 = '绝对魅力'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['魔灵召唤：波拉斯','魔灵召唤：瓦尔琪','魔灵召唤：狂暴布洛克','魔灵召唤：假面杰森','魔灵召唤：大画家芭芘','魔灵召唤：旋转小冯','魔灵召唤：小吸血鬼夏伊','魔灵召唤：大富翁鲁邦','魔灵召唤：迪克老爹','魔灵召唤：红心女王艾丽莎']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.012 * self.等级, 5)    

    自定义描述 = 1
    描述 = ''
    def 技能描述(self, 武器类型):
        temp = ''
        temp += '加成倍率：%.1f%%' % (3.5 + 1.2 * self.等级) + '<br>'
        temp += '关联技能：魔灵召唤系列,'
        temp += self.描述 + ',魔灵炸弹(部分),毁灭突进(部分)'
        return temp    

class 黑曜神技能6(主动技能):
    名称 = '魔灵召唤：假面杰森'
    备注 = '(每秒DPS)'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 800.21
    成长 = 34.68
    攻击次数 = 8/7/20
    #数据1 = [0, 1418, 1547, 1682, 1814, 1947, 2079, 2211, 2344, 2476, 2609, 2741, 2874, 3005, 3137, 3277, 3409, 3542, 3674, 3806, 3938, 4074, 4207, 4338, 4467, 4599, 4731, 4868, 5000, 5133, 5264, 5396, 5532, 5665, 5797, 5929, 6062, 6194, 6326, 6458, 6591, 6723, 6855, 6988, 7127, 7259, 7392, 7520, 7652, 7784, 7920, 8052, 8185, 8317, 8449, 8582, 8717, 8850, 8982, 9114, 9247, 9382, 9514, 9647, 9779, 9912, 10044, 10175, 10308, 10440, 10572]
    #攻击次数1 = 6
    #数据2 = [0, 284, 310, 337, 364, 390, 416, 442, 469, 496, 522, 548, 574, 600, 627, 655, 681, 708, 734, 761, 788, 815, 842, 868, 894, 921, 946, 974, 1000, 1027, 1053, 1079, 1106, 1133, 1160, 1186, 1212, 1238, 1265, 1292, 1319,  1345, 1371, 1398, 1426, 1452, 1479, 1504, 1531, 1557, 1584, 1610, 1637, 1663, 1690, 1716, 1743, 1770, 1797, 1823, 1849, 1877, 1903, 1930, 1956, 1982, 2009, 2035, 2062, 2088, 2114]
    #攻击次数2 = 2
    TP成长 = 0.10
    TP上限 = 5
    def 等效CD(self, 武器类型):
        return 1.0
        
class 黑曜神技能7(主动技能):
    名称 = '魔灵召唤：大画家芭芘'
    备注 = '(每秒DPS)'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 435.41
    成长 = 18.88
    攻击次数 = 14/5/20
    #数据1 = [0, 280, 307, 334, 360, 385, 412, 437, 464, 491, 517, 544, 569, 596, 622, 650, 676, 701, 727, 754, 780, 807, 833, 860, 885, 911, 938, 964, 991, 1016, 1043, 1069, 1095, 1122, 1148, 1175, 1202, 1227, 1254, 1280, 1305, 1332, 1359, 1384, 1412, 1437, 1464, 1490, 1517, 1543, 1569, 1595, 1622, 1648, 1674, 1700, 1726, 1752, 1779, 1805, 1832, 1859, 1885, 1911, 1937, 1963, 1990, 2016, 2042, 2068, 2093]
    #攻击次数1 = 12
    #数据2 = [0, 365, 398, 432, 467, 500, 535, 569, 603, 637, 671, 706, 740, 773, 808, 843, 878, 911, 946, 979, 1013, 1049, 1083, 1116, 1149, 1183, 1217, 1252, 1286, 1319, 1355, 1388, 1423, 1456, 1491, 1526, 1560, 1594, 1629, 1662, 1696, 1730, 1764, 1798, 1833, 1868, 1901, 1935, 1969, 2003, 2038, 2072, 2105, 2139, 2174, 2207, 2242, 2276, 2310, 2345, 2379, 2414, 2447, 2481, 2516, 2550, 2584, 2619, 2651, 2686, 2719]
    #攻击次数2 = 2
    #复制伤害数据3 = [0, 1184, 1293, 1406, 1517, 1626, 1738, 1848, 1959, 2072, 2182, 2292, 2404, 2514, 2624, 2739, 2850, 2961,3073, 3182, 3292, 3405, 3516, 3626, 3736, 3846, 3956, 4068, 4180, 4290, 4401, 4511, 4623, 4734, 4846, 4955,5066, 5177, 5290, 5400, 5512, 5622, 5732, 5843, 5959, 6069, 6179, 6287, 6398, 6510, 6622, 6732, 6844, 6953,7063, 7175, 7288, 7398, 7509, 7619, 7729, 7842, 7953, 8064, 8174, 8285, 8398, 8509, 8617, 8727, 8838]
    TP成长 = 0.10
    TP上限 = 5
    def 等效CD(self, 武器类型):
        return 1.0
        
class 黑曜神技能8(主动技能):
    名称 = '魔灵召唤：旋转小冯'
    备注 = '(每秒DPS)'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 1444.80
    成长 = 61.64
    攻击次数 = 73/90/20
    #数据1 = [0, 190, 208, 227, 244, 262, 279, 297, 314, 332, 350, 368, 385, 403, 421, 440, 457, 476, 493, 511, 529, 547, 564, 582, 599, 617, 635, 653, 671, 689, 707, 725, 743, 760, 778, 796, 814, 833, 850, 867, 885, 903, 921, 938, 957, 975, 992, 1010, 1028, 1045, 1063, 1080, 1099, 1117, 1135, 1151, 1170, 1188, 1206, 1223, 1241, 1259, 1277, 1295, 1313, 1330, 1349, 1366, 1383, 1401, 1418]
    #攻击次数1 = 9 * 5
    #数据2 = [0, 245, 268, 291, 314, 337, 360, 381, 404, 428, 451, 473, 497, 519, 543, 565, 589, 611, 635, 657, 680, 702, 725, 748, 771, 794, 817, 840, 863, 886, 908, 931, 954, 977, 1000, 1022, 1046, 1068, 1092, 1114, 1138, 1160, 1184, 1206, 1230, 1252, 1275, 1298, 1321, 1344, 1366, 1390, 1412, 1436, 1458, 1481, 1505, 1527, 1550, 1573, 1595, 1618, 1641, 1664, 1687, 1710, 1734, 1757, 1778, 1802, 1823]
    #攻击次数2 = 3 * 6
    #数据3 = [0, 339, 371, 402, 436, 467, 499, 529, 562, 594, 626, 657, 689, 721, 752, 786, 817, 849, 880, 913, 943, 977, 1009, 1040, 1070, 1103, 1134, 1166, 1197, 1230, 1262, 1293, 1326, 1358, 1390, 1420, 1454, 1484, 1517, 1548, 1580, 1611, 1643, 1675, 1709, 1740, 1771, 1803, 1833, 1867, 1900, 1931, 1961, 1994, 2026, 2057, 2089, 2120, 2152, 2184, 2216, 2248, 2280, 2313, 2344, 2374, 2408, 2439, 2471, 2502, 2534]
    #攻击次数3 = 1 * 10
    TP成长 = 0.10
    TP上限 = 5
    def 等效CD(self, 武器类型):
        return 1.0
        
class 黑曜神技能9(主动技能):
    名称 = '魔灵召唤：小吸血鬼夏伊'
    备注 = '(每秒DPS)'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 711.37
    成长 = 30.36
    攻击次数 = 14/3/20
    #数据1 = [0, 507, 554, 602, 649, 697, 743, 791, 839, 887, 933, 982, 1029, 1076, 1123, 1173, 1220, 1267, 1315, 1363, 1409, 1458, 1506, 1553, 1599, 1645, 1694, 1742, 1788, 1837, 1885, 1931, 1979, 2028, 2075, 2121, 2169, 2217, 2264, 2313, 2359, 2407, 2453, 2501, 2552, 2598, 2644, 2691, 2740, 2787, 2834, 2882, 2930, 2976, 3025, 3071, 3120, 3167, 3214, 3262, 3309, 3357, 3405, 3452, 3500, 3547, 3596, 3643, 3689, 3736, 3783]
    #攻击次数1 = 10
    #数据2 = [0, 543, 594, 645, 697, 747, 797, 848, 899, 950, 1001, 1051, 1103, 1153, 1204, 1256, 1307, 1358, 1409, 1460, 1510, 1563, 1614, 1665, 1713, 1763, 1814, 1867, 1917, 1968, 2019, 2070, 2120, 2172, 2222, 2273, 2324, 2375, 2427, 2479, 2527, 2579, 2629, 2680, 2734, 2784, 2834, 2885, 2935, 2986, 3038, 3089, 3139, 3191, 3241, 3291, 3344, 3393, 3443, 3495, 3545, 3598, 3649, 3700, 3750, 3802, 3852, 3903, 3954, 4003, 4054]
    #攻击次数2 = 3
    #数据3 = [0, 1356, 1484, 1611, 1738, 1867, 1994, 2118, 2245, 2374, 2502, 2629, 2756, 2882, 3009, 3141, 3267, 3394, 3522, 3649, 3776, 3905, 4032, 4159, 4281, 4408, 4535, 4665, 4792, 4919, 5046, 5173, 5303, 5430, 5557, 5684,  5811, 5938, 6067, 6194, 6318, 6445, 6572, 6699, 6834, 6958, 7085, 7210, 7337, 7464, 7594, 7721, 7848, 7974, 8102, 8225, 8357, 8483, 8609, 8736, 8863, 8994, 9121, 9248, 9374, 9500, 9629, 9756, 9881, 10007, 10134]
    #攻击次数3 = 1
    TP成长 = 0.10
    TP上限 = 5
    def 等效CD(self, 武器类型):
        return 1.0
        
class 黑曜神技能10(主动技能):
    名称 = '魔灵召唤：大富翁鲁邦'
    备注 = '(每秒DPS)'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 1024.96
    成长 = 38.23
    攻击次数 = 18/5/20
    #data1 = [0, 528, 564, 600, 636, 673, 709, 745, 781, 817, 852, 890, 926, 962, 998, 1034, 1069, 1107, 1142, 1179, 1213, 1249, 1285, 1322, 1358, 1394, 1430, 1466, 1502, 1538, 1575, 1610, 1646, 1683, 1719, 1755, 1790, 1827, 1862, 1898, 1936, 1971, 2007, 2043, 2079, 2115, 2152, 2187, 2224, 2260, 2296, 2330, 2369, 2404, 2440, 2476, 2512, 2548, 2584, 2621, 2656, 2692, 2729, 2765, 2800, 2836, 2872, 2909, 2946, 2981, 3017]
    #data2 = [0, 1163, 1242, 1321, 1400, 1480, 1559, 1639, 1717, 1797, 1875, 1958, 2038, 2117, 2196, 2275, 2354, 2435, 2514, 2593, 2669, 2749, 2828, 2908, 2987, 3067, 3145, 3226, 3305, 3384, 3464, 3542, 3622, 3702, 3782, 3860, 3938, 4019, 4097, 4177, 4260, 4338, 4416, 4494, 4574, 4654, 4733, 4811, 4892, 4970, 5049, 5128, 5210, 5287, 5367, 5445, 5525, 5606, 5684, 5765, 5844, 5922, 6004, 6082, 6160, 6237, 6317, 6398, 6479, 6557, 6637]
    #data3 = [0, 1743, 1862, 1982, 2100, 2219, 2338, 2458, 2577, 2695, 2813, 2937, 3056, 3175, 3293, 3412, 3531, 3652, 3770, 3889, 4003, 4122, 4242, 4362, 4480, 4602, 4719, 4837, 4957, 5078, 5196, 5315, 5432, 5552, 5673, 5792, 5908, 6028, 6145, 6263, 6390, 6505, 6624, 6741, 6861, 6980, 7100, 7219, 7337, 7456, 7574, 7691, 7815, 7932, 8051, 8168, 8288, 8408, 8527, 8646, 8764, 8883, 9005, 9123, 9240, 9356, 9474, 9596, 9717, 9835, 9954]
    #data4 = [0, 627, 671, 713, 755, 799, 842, 885, 927, 969, 1013, 1057, 1099, 1143, 1186, 1228, 1272, 1315, 1357, 1400, 1441, 1485, 1527, 1571, 1613, 1656, 1698, 1742, 1785, 1828, 1870, 1913, 1956, 1999, 2042, 2085, 2127, 2170, 2212, 2255, 2300, 2343, 2384, 2426, 2471, 2512, 2556, 2598, 2641, 2686, 2727, 2769, 2813, 2855, 2898, 2940, 2984, 3028, 3070, 3112, 3155, 3198, 3241, 3284, 3327, 3369, 3411, 3455, 3498, 3541, 3583]
    #数据 = [data1, data2, data3, data4]
    #次数 = [8, 4, 1, 1*5,]
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型):
        return 1.0

    #def 等效百分比(self, 武器类型):
        #sum = 0
        #for i in range(4):
            #sum += self.数据[i][self.等级] * self.次数[i]
        #return sum * self.倍率
        
class 黑曜神技能11(主动技能):
    名称 = '魔灵召唤：迪克老爹'
    备注 = '(每秒DPS)'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 1179.84
    成长 = 55.34
    攻击次数 = 8/1.8/20
    #数据1 = [0, 680, 749, 818, 887, 957, 1025, 1094, 1163, 1232, 1301, 1370, 1439, 1508, 1577, 1646, 1715, 1784, 1853, 1922, 1991, 2060, 2129, 2198, 2267, 2336, 2405, 2474, 2543, 2612, 2680, 2750, 2819, 2888, 2957, 3026, 3094, 3164, 3233, 3302, 3371, 3440, 3508, 3578, 3647, 3715, 3785, 3853, 3923, 3992, 4061, 4129, 4199, 4268, 4337, 4406, 4475, 4543, 4613, 4682, 4751, 4820, 4889, 4958, 5027, 5096, 5164, 5234, 5302, 5371, 5441]
    #攻击次数1 = 10
    #数据2 = [0, 1941, 2138, 2335, 2533, 2730, 2926, 3123, 3319, 3516, 3714, 3911, 4108, 4305, 4501, 4699, 4896, 5092, 5289, 5486, 5684, 5881, 6077, 6274, 6471, 6668, 6865, 7061, 7259, 7456, 7653, 7850, 8046, 8243, 8440, 8637, 8834, 9031, 9229, 9425, 9622, 9819, 10015, 10213, 10409, 10607, 10805, 11000, 11197, 11395, 11591, 11789, 11985, 12182, 12380, 12576, 12773, 12970, 13166, 13364, 13561, 13757, 13955, 14152, 14349, 14546, 14742, 14939, 15136, 15333, 15530]
    #攻击次数2 = 2
    #数据3 = [0, 2448, 2696, 2945, 3193, 3442, 3690, 3938, 4186, 4434, 4684, 4931, 5180, 5429, 5676, 5925, 6174, 6422, 6670, 6918, 7167, 7415, 7663, 7912, 8160, 8408, 8657, 8906, 9153, 9402, 9650, 9898, 10147, 10395, 10643, 10892, 11140, 11389, 11637, 11885, 12134, 12382, 12631, 12879, 13127, 13375, 13624, 13872, 14120, 14369, 14617, 14865, 15114, 15362, 15611, 15859, 16107, 16356, 16603, 16853, 17101, 17348, 17598, 17846, 18094, 18342, 18590, 18839, 19087, 19336, 19584]
    #攻击次数3 = 1
    TP成长 = 0.10
    TP上限 = 5
    def 等效CD(self, 武器类型):
        return 1.0
        
class 黑曜神技能12(主动技能):
    名称 = '魔灵召唤：红心女王艾丽莎'
    备注 = '(每秒DPS)'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    基础 = 1647.65
    成长 = 76.20
    攻击次数 = 12/1.8/20
    #数据1 = [0, 2293, 2525, 2759, 2991, 3223, 3455, 3688, 3921, 4154, 4387, 4619, 4851, 5083, 5317, 5549, 5781, 6015, 6247, 6479, 6712, 6945, 7177, 7410, 7643, 7875, 8108, 8339, 8573, 8806, 9038, 9271, 9504, 9735, 9968, 10202, 10434, 10666, 10899, 11131, 11363, 11597, 11830, 12062, 12294, 12527, 12759, 12992, 13225, 13458, 13690, 13922, 14155, 14387, 14621, 14853, 15086, 15318, 15550, 15783, 16016, 16249, 16480, 16714, 16946, 17178, 17411, 17645, 17876, 18109, 18342]
    #攻击次数1 = 6*0.795
    #数据2 = [0, 2523, 2778, 3035, 3290, 3545, 3801, 4057, 4314, 4569, 4825, 5081, 5336, 5592, 5849, 6105, 6359, 6616, 6872, 7127, 7384, 7640, 7894, 8150, 8407, 8663, 8919, 9174, 9430, 9686, 9941, 10198, 10454, 10709, 10965, 11222, 11477, 11732, 11989, 12245, 12500, 12757, 13012, 13268, 13523, 13780, 14036, 14292, 14547, 14803, 15059, 15314, 15571, 15827, 16083, 16338, 16594, 16850, 17105, 17362, 17618, 17873, 18128, 18385, 18641, 18896, 19153, 19409, 19663, 19920, 20176]
    #攻击次数2 = 3*0.795
    TP成长 = 0.10
    TP上限 = 5
    def 等效CD(self, 武器类型):
        return 1.0
        
class 黑曜神技能13(主动技能):
    名称 = '军团列阵'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 3
    等级精通 = 60
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 4025, 4661, 5305, 5947, 6590, 7232, 7870, 8513, 9155, 9797, 10440, 11078, 11721, 12363, 13006, 13644, 14286, 14929,15572, 16215, 16851, 17495, 18137, 18780, 19423, 20060, 20703, 21346, 21988, 22631, 23270, 23912, 24553, 25197, 25834, 26477, 27120, 27763, 28405, 29042, 29685, 30328, 30971, 31614, 32251, 32893, 33537, 34178, 34821, 35460, 36102, 36743, 37387, 38025, 38667, 39310, 39953, 40595, 41233, 41875, 42518, 43161, 43804, 44441, 45084, 45727, 46369, 47008, 47650, 48292]
    攻击次数 = 1
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 黑曜神技能14(主动技能):
    名称 = '连锁共振'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 1
    CD = 6
    TP成长 = 0.10
    TP上限 = 5
    关联技能 = ['魔灵召唤：波拉斯','魔灵召唤：瓦尔琪','魔灵召唤：狂暴布洛克','魔灵召唤：假面杰森','魔灵召唤：旋转小冯','魔灵召唤：迪克老爹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 7:
                return round(1.94 + 0.02 * self.等级, 5)
            else:
                return round(2.1 + 0 * (self.等级 - 7), 5)

class 黑曜神技能15(主动技能):
    名称 = '魔灵炸弹'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 546, 602, 658, 715, 771, 828, 884, 940, 998, 1054, 1111, 1167, 1223, 1280, 1336, 1392, 1449, 1505, 1562, 1618, 1674, 1731, 1788, 1844, 1899, 1956, 2013, 2071, 2127, 2183, 2239, 2296, 2353, 2409, 2465, 2521, 2578, 2634, 2690, 2746, 2804, 2860, 2916, 2972, 3029, 3086, 3141, 3197, 3254, 3311, 3368, 3425, 3481, 3538, 3594, 3651, 3707, 3763, 3820, 3876, 3932, 3988, 4045, 4102, 4158, 4214, 4271, 4327, 4383, 4439]#jio踢
    攻击次数1 = 1
    数据2 = [0, 7621, 8393, 9166, 9940, 10711, 11486, 12258, 13032, 13805, 14578, 15351, 16124, 16897, 17669, 18443, 19216, 19990, 20763, 21538, 22309, 23085, 23855, 24626, 25401, 26174, 26948, 27721, 28496, 29270, 30043, 30815, 31588, 32359, 33133, 33905, 34679, 35454, 36228, 37000, 37773, 38549, 39320, 40090, 40865, 41637, 42413, 43185, 43958, 44731, 45507, 46278, 47050, 47823, 48596, 49370, 50143, 50916, 51688, 52464, 53236, 54008, 54781, 55554, 56330, 57101, 57876, 58646, 59422, 60196, 60966]#大爹
    攻击次数2 = 1
    #数据3 = [0, 6065, 6690, 7301, 7920, 8536, 9158, 9770, 10373, 10988, 11610, 12228, 12840, 13454, 14075, 14691, 15309, 15921, 16534, 17152, 17774, 18379, 19001, 19617, 20232, 20843, 21460, 22083, 22699, 23303, 23931, 24545, 25166, 25771, 26383, 27009, 27621, 28235, 28851, 29465, 30091, 30702, 31305, 31929, 32545, 33170, 33774, 34400, 35014, 35625, 36244, 36853, 37465, 38094, 38697, 39319, 39932, 40562, 41166, 41782, 42390, 43022, 43633, 44244, 44857, 45486, 46101, 46710, 47321, 47944, 48553]鸭子爆炸旋风5hit
    #攻击次数3 = 1
    CD = 12

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 黑曜神技能16(主动技能):
    名称 = '魔幻旋风'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 722, 796, 869, 943, 1016, 1089, 1163, 1236, 1309, 1383, 1456, 1529, 1604, 1677, 1750, 1823, 1896, 1970, 2043, 2117, 2190, 2263, 2337, 2410, 2483, 2556, 2630, 2703, 2777, 2851, 2924, 2996, 3070, 3143, 3217, 3290, 3364, 3437, 3510, 3584, 3657, 3730, 3804, 3877, 3950, 4024, 4098, 4170, 4243, 4317, 4391, 4463, 4538, 4611, 4684, 4757, 4831, 4904, 4977, 5051, 5124, 5198, 5271, 5344, 5417, 5490, 5564, 5638, 5711, 5785]
    攻击次数1 = 1
    数据2 = [0, 242, 266, 291, 316, 339, 364, 389, 413, 437, 462, 487, 512, 536, 561, 585, 609, 634, 659, 683, 707, 732, 757, 781, 806, 830, 855, 878, 904, 929, 952, 977, 1002, 1027, 1051, 1075, 1100, 1124, 1149, 1174, 1199, 1222, 1247, 1272, 1297, 1320, 1345, 1370, 1393, 1419, 1444, 1469, 1492, 1517, 1542, 1566, 1590, 1615, 1640, 1663, 1689, 1714, 1738, 1762, 1787, 1812, 1836, 1860, 1885, 1910, 1935]#多段攻击
    攻击次数2 = 14
    CD = 7
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 黑曜神技能17(主动技能):
    名称 = '毁灭突进'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 2732, 3004, 3282, 3563, 3839, 4117, 4387, 4665, 4946, 5225, 5500, 5778, 6052, 6333, 6605, 6883, 7160, 7439, 7713, 7991, 8268, 8543, 8828, 9098, 9379, 9652, 9930, 10209, 10484, 10759, 11035, 11315, 11595, 11864, 12146, 12423, 12696, 12977, 13255, 13532, 13805, 14082, 14359, 14640, 14911, 15188, 15466, 15747, 16023, 16297, 16576, 16848, 17128, 17408, 17683, 17957, 18234, 18512, 18793, 19065, 19346, 19627, 19898, 20176, 20448, 20729, 21006, 21283, 21560, 21836]#突进和最后一击
    攻击次数1 = 2
    数据2 = [0, 76, 84, 91, 100, 108, 116, 123, 131, 138, 146, 154, 161, 170, 178, 185, 193, 201, 208, 216, 223, 231, 239, 248, 255, 263, 270, 278, 286, 293, 301, 309, 317, 325, 332, 340, 348, 355, 363, 371, 378, 387, 395, 402, 410, 418, 425, 433, 441, 448, 457, 465, 472, 480, 487, 495, 503, 510, 518, 526, 534, 542, 550, 557, 565, 572, 580, 588, 596, 604, 612]
    攻击次数2 = 5
    数据3 = [0, 230, 252, 275, 300, 323, 346, 369, 392, 415, 439, 462, 485, 509, 532, 555, 578, 602, 625, 648, 671, 694, 717, 742, 764, 787, 811, 834, 857, 881, 904, 927, 951, 974, 996, 1021, 1044, 1066, 1090, 1113, 1136, 1160, 1183, 1206, 1230, 1253, 1276, 1300, 1323, 1346, 1369, 1393, 1415, 1439, 1462, 1485, 1509, 1532, 1555, 1578, 1602, 1625, 1648, 1672, 1695, 1717, 1742, 1764, 1787, 1811, 1834]
    攻击次数3 = 5
    CD = 12
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 黑曜神技能18(主动技能):
    名称 = '翔空剑'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 904, 996, 1087, 1178, 1271, 1362, 1454, 1546, 1638, 1730, 1821, 1913, 2004, 2096, 2188, 2280, 2372, 2463, 2556,2647, 2738, 2830, 2922, 3013, 3105, 3197, 3290, 3381, 3473, 3563, 3656, 3748, 3839, 3932, 4023, 4114, 4206, 4299,4391, 4481, 4572, 4665, 4757, 4849, 4941, 5033, 5124, 5215, 5307, 5399, 5490, 5582, 5674, 5766, 5858, 5951, 6042,6132, 6224, 6316, 6409, 6500, 6591, 6684, 6775, 6867, 6958, 7050, 7142, 7233]#跳斩伤害
    攻击次数1 = 1
    数据2 = [0, 355, 392, 428, 464, 500, 537, 573, 609, 644, 681, 717, 753, 789, 826, 862, 898, 933, 970, 1007, 1042, 1078, 1115, 1150, 1187, 1223, 1259, 1295, 1332, 1367, 1404, 1440, 1475, 1513, 1549, 1584, 1620, 1657, 1693, 1729, 1764, 1802, 1838, 1873, 1909, 1947, 1982, 2018, 2053, 2090, 2127, 2162, 2198, 2235, 2270, 2307, 2343, 2379, 2415, 2452, 2487, 2524, 2560, 2595, 2632, 2668, 2704, 2740, 2776, 2813, 2849]#多段伤害
    攻击次数2 = 15
    数据3 = [0, 4017, 4427, 4835, 5246, 5656, 6062, 6470, 6879, 7286, 7697, 8107, 8515, 8921, 9331, 9743, 10150, 10557, 10967, 11375, 11784, 12196, 12602, 13012, 13420, 13832, 14237, 14645, 15056, 15462, 15873, 16279, 16690, 17101, 17508, 17918, 18323, 18733, 19140, 19554, 19960, 20368, 20776, 21185, 21594, 22003, 22414, 22823, 23229, 23640, 24050, 24458, 24866, 25275, 25682, 26090, 26501, 26909, 27319, 27726, 28134, 28543, 28953, 29361, 29773, 30180, 30588, 30996, 31406, 31813, 32226]#其余伤害整合
    攻击次数3 = 1
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * (self.攻击次数2 + self.TP等级) + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    #def 等效百分比(self, 武器类型):
        #return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.23

class 黑曜神技能19(主动技能):
    名称 = '碎灵屠戮'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 7029, 7760, 8484, 9212, 9936, 10664, 11396, 12120, 12847, 13571, 14304, 15025, 15751, 16463, 17191, 17938, 18661, 19388, 20099, 20825, 21572, 22295, 23024, 23730, 24476, 25185, 25914, 26638, 27366, 28112, 28821, 29552, 30274, 31002, 31746, 32457, 33174, 33904, 34639, 35362, 36088, 36812, 37539, 38273, 38996, 39725, 40447, 41175, 41909, 42629, 43353, 44079, 44813, 45536, 46263, 46988, 47714, 48447, 49170, 49900, 50623, 51332, 52076, 52804, 53526, 54255, 54988, 55713, 56439, 57163]#挥斩伤害
    攻击次数1 = 1
    数据2 = [0, 39487, 43492, 47482, 51487, 55470, 59479, 63478, 67454, 71454, 75465, 79448, 83449, 87449, 91448, 95453, 99429, 103431, 107428, 111434, 115440, 119411, 123415, 127405, 131416, 133757, 139410, 143412, 147406, 151398, 155393, 159400, 163397, 167391, 171374, 175365, 179378, 183382, 187372, 191365, 195367, 199369, 203348, 207351, 211336, 215352, 219336, 223342, 227343, 231332, 235334, 239324, 243315, 247325, 251311, 255313, 259304, 263314, 267298, 271298, 275287, 279297, 283300, 287279, 291281, 295286, 299282, 303271, 307270, 311268, 315257]#爆炸整合
    攻击次数2 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.25
        self.CD *= 0.9

class 黑曜神技能20(主动技能):
    名称 = '聚灵升空剑'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 1892, 2084, 2277, 2470, 2661, 2852, 3045, 3237, 3430, 3621, 3813, 4005, 4198, 4389, 4581, 4773, 4966, 5158, 5349, 5541, 5734, 5926, 6118, 6309, 6502, 6693, 6887, 7078, 7270, 7462, 7653, 7847, 8038, 8230, 8422, 8615, 8806, 9000, 9190, 9383, 9575, 9766, 9960, 10151, 10344, 10535, 10727, 10919, 11110, 11304, 11495, 11687, 11879, 12072, 12264, 12455, 12647,12840, 13032, 13223, 13416, 13608, 13800, 13992, 14183, 14376, 14568, 14761, 14952, 15145]
    攻击次数1 = 1
    数据2 = [0, 2272, 2502, 2732, 2963, 3193, 3423, 3654, 3885, 4116, 4346, 4576, 4807, 5037, 5267, 5497, 5729, 5959, 6189, 6420, 6650, 6880, 7111, 7341, 7572, 7803, 8033, 8263, 8494, 8724, 8954, 9185, 9415, 9647, 9877, 10107, 10337, 10568, 10798, 11029, 11260, 11490, 11720, 11951, 12181, 12412, 12641, 12872, 13103, 13334, 13564, 13795, 14025, 14255, 14485, 14717, 14948, 15177, 15408, 15637, 15869, 16099, 16328, 16560, 16791, 17021, 17252, 17482, 17712, 17942, 18173]
    攻击次数2 = 5
    数据3 = [0, 5680, 6255, 6831, 7407, 7984, 8559, 9137, 9712, 10287, 10864, 11441, 12016, 12593, 13169, 13745, 14322, 14898, 15472, 16050, 16626, 17202, 17777, 18354, 18930, 19506, 20083, 20659, 21235, 21811, 22388, 22963, 23540, 24115, 24693, 25268, 25845, 26420, 26997, 27574, 28149, 28726, 29301, 29877, 30453, 31031, 31606, 32181, 32758, 33334, 33910, 34488, 35062,35639, 36216, 36791, 37367, 37944, 38520, 39096, 39673, 40248, 40824, 41401, 41977, 42553, 43129, 43705, 44282, 44857, 45434]
    攻击次数3 = 1
    CD = 40.0
    TP成长 = 0
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * (self.攻击次数2 + self.TP等级) + self.数据3[self.等级] * self.攻击次数3) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.23

class 黑曜神技能21(被动技能):
    名称 = '魔能榨取'
    所在等级 = 48
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 16:
                return round(1.015 + 0.015 * self.等级, 5)
            else:
                return round(1.295 + 0.020 * (self.等级 - 16), 5)

class 黑曜神技能22(主动技能):
    名称 = '魔神百裂拳'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 1598, 1969, 2339, 2711, 3081, 3451, 3821, 4192, 4562, 4934, 5303, 5675, 6046, 6416, 6787, 7156, 7528, 7898, 8270, 8639, 9010, 9381, 9751, 10121, 10492, 10863, 11234, 11605, 11975, 12346, 12716, 13087, 13457, 13828, 14198, 14569, 14940,15311, 15682, 16052, 16422, 16793, 17164, 17534, 17905, 18275, 18647, 19017, 19387, 19757]
    攻击次数1 = 12
    攻击倍率1 = 1.1
    数据2 = [0, 9589, 11813, 14036, 16260, 18484, 20708, 22931, 25155, 27379, 29602, 31826, 34049, 36273, 38498, 40721, 42944, 45169, 47392, 49616, 51839, 54063, 56287, 58511, 60734, 62957, 65182, 67406, 69628, 71852, 74077, 76300, 78524, 80747, 82971, 85195, 87418, 89641, 91867, 94090, 96313, 98537, 100760, 102984, 105208, 107432, 109655, 111879, 114103, 116326, 118550]
    攻击次数2 = 1
    攻击倍率2 = 1.0
    数据3 = [0, 6391, 7875, 9355, 10839, 12320, 13804, 15285, 16770, 18250, 19734, 21215, 22699, 24182, 25663, 27147, 28627, 30112,31592, 33077, 34556, 36041, 37522, 39005, 40486, 41970, 43455, 44935, 46420, 47900, 49384, 50864, 52349, 53829, 55313, 56794, 58278, 59758, 61242, 62727, 64206, 65691, 67172, 68656, 70136, 71621, 73101, 74585, 76066, 77550, 79030]
    攻击次数3 = 3
    攻击倍率3 = 1.1
    CD = 145

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.攻击倍率1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率2 + self.数据3[self.等级] * self.攻击次数3* self.攻击倍率3) * (1 + self.TP成长 * self.TP等级) * self.倍率

        
class 黑曜神技能23(主动技能):
    名称 = '黑暗冲击'
    备注 = '(完全打满)'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 1208, 1330, 1453, 1575, 1698, 1820, 1943, 2065, 2188, 2310, 2433, 2555, 2678, 2800, 2923, 3045, 3168, 3290, 3413, 3535, 3658, 3780, 3904, 4026, 4149, 4271, 4394, 4516, 4639, 4761, 4884, 5006, 5129, 5251, 5374, 5496, 5619, 5742, 5864, 5987, 6109, 6232, 6354, 6477, 6599, 6722, 6845, 6967, 7090, 7213]
    攻击次数1 = 4
    数据2 = [0, 960, 1057, 1156, 1252, 1350, 1447, 1545, 1642, 1740, 1837, 1935, 2032, 2130, 2227, 2325, 2422, 2519, 2617, 2714, 2811, 2908, 3007, 3104, 3201, 3298, 3397, 3494, 3591, 3688, 3786, 3884, 3981, 4078, 4176, 4273, 4371, 4468, 4566, 4663, 4761, 4858, 4955, 5053, 5150, 5248, 5345, 5443, 5540, 5637, 5735]
    攻击次数2 = 9
    数据3 = [0, 1912, 2106, 2300, 2494, 2687, 2881, 3076, 3270, 3463, 3658, 3852, 4045, 4240, 4434, 4628, 4821, 5015, 5209, 5404, 5597, 5791, 5986, 6180, 6373, 6567, 6762, 6955, 7149, 7343, 7537, 7731, 7925, 8119, 8314, 8507, 8701, 8895, 9090, 9283, 9477, 9671, 9865, 10058, 10253, 10447, 10641, 10835, 11029, 11223, 11417]
    攻击次数3 = 3
    CD = 30
    TP成长 = 0.12
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.15

class 黑曜神技能24(主动技能):
    名称 = '午夜嘉年华'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 1089, 1201, 1311, 1422, 1530, 1642, 1752, 1863, 1973, 2084, 2194, 2305, 2415, 2526, 2637, 2747, 2856, 2967, 3080, 3189, 3299, 3410, 3521, 3631, 3742, 3852, 3962, 4074, 4184, 4294, 4404, 4516, 4625, 4736, 4848, 4958, 5068, 5179, 5287, 5400, 5510, 5620, 5732, 5841, 5951, 6063, 6174, 6283, 6395, 6505]
    攻击次数 = 31
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.09
        self.攻击次数 += 4

class 黑曜神技能25(被动技能):
    名称 = '亚丁之力'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    关联技能 = ['魔幻旋风','毁灭突进','翔空剑','聚灵升空剑','魔神百裂拳','黑暗冲击','午夜嘉年华','绚丽耀光','魔灵乱舞','黑曜之眸：亚丁降临']
    关联技能2 = ['魔灵召唤：波拉斯','魔灵召唤：瓦尔琪','魔灵召唤：狂暴布洛克','魔灵召唤：假面杰森','魔灵召唤：大画家芭芘','魔灵召唤：旋转小冯','魔灵召唤：小吸血鬼夏伊','魔灵召唤：大富翁鲁邦','魔灵召唤：迪克老爹','魔灵召唤：红心女王艾丽莎']
  
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.28 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.14 + 0.02 * self.等级, 5)

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 黑曜神技能26(主动技能):
    名称 = '绚丽耀光'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据1 = [0, 15307, 16860, 18413, 19966, 21519, 23072, 24625, 26178, 27731, 29284, 30837, 32389, 33943, 35496, 37048, 38602, 40155, 41707, 43261, 44813, 46366, 47920, 49472, 51025, 52578, 54131, 55684, 57237, 58790, 60343, 61896, 63449, 65002, 66554, 68108, 69660, 71213, 72767, 74319, 75872, 77426, 78978, 80531, 82084, 83637, 85190, 86743, 88296, 89849, 91402, 92955, 94508, 96061, 97614, 99166, 100720, 102273, 103825, 105379, 106931, 108484, 110038, 111590, 113143, 114697, 116249, 117802, 119355, 120908, 122461]
    攻击次数1 = 1
    数据2 = [0, 3571, 3934, 4296, 4659, 5021, 5384, 5746, 6108, 6470, 6833, 7195, 7558, 7920, 8282, 8644, 9007, 9369, 9732, 10094, 10456, 10819, 11181, 11544, 11906, 12269, 12631, 12993, 13355, 13718, 14080, 14443, 14805, 15167, 15529, 15892, 16254, 16617, 16979, 17341, 17703, 18066, 18428, 18791, 19153, 19516, 19877, 20240, 20602, 20965, 21327, 21690, 22052, 22414, 22776, 23139, 23501, 23864, 24226, 24588, 24950, 25313, 25675, 26038, 26400, 26762, 27124, 27487, 27849, 28212, 28574]
    攻击次数2 = 10
    CD = 40.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 黑曜神技能27(主动技能):
    名称 = '魔灵乱舞'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 5018, 5528, 6037, 6545, 7055, 7564, 8073, 8582, 9092, 9600, 10110, 10619, 11127, 11637, 12147, 12655, 13165,13674,14182, 14692, 15201, 15710, 16220, 16728, 17237, 17747, 18255, 18765, 19275, 19783, 20292, 20802, 21310, 21820,22329, 22838, 23347, 23857, 24365, 24874, 25384, 25893, 26402, 26911, 27420, 27929, 28439, 28948, 29457, 29966,30475, 30984, 31493, 32003, 32512, 33020, 33530, 34039, 34548, 35058, 35567, 36075, 36585, 37094, 37602, 38113,38622, 39130, 39640, 40149]
    攻击次数 = 12
    CD = 50.0

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 黑曜神技能28(主动技能):
    名称 = '黑曜之眸：亚丁降临'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 9692, 11938, 14184, 16432, 18680, 20929, 23174, 25424, 27669, 29916, 32165, 34414, 36661, 38910, 41155, 43402, 45650, 47899, 50147, 52394, 54638, 56887, 59136, 61383, 63631, 65881, 68123, 70372, 72622, 74868, 77117, 79367, 81610, 83858, 86105, 88354, 90603, 92849, 95095, 97345, 99590, 101840, 104090, 106335, 108585, 110830, 113077, 115326, 117572, 119821, 122070, 124313, 126562, 128810, 131058, 133307, 135555, 137799, 140046, 142294, 144544, 146791, 149039, 151284, 153533, 155781, 158029, 160278, 162525, 164769]
    攻击次数1 = 11
    数据2 = [0, 401, 494, 586, 680, 773, 866, 959, 1051, 1144, 1237, 1330, 1423, 1516, 1609, 1702, 1795, 1887, 1981, 2074, 2167, 2260, 2353, 2446, 2538, 2631, 2724, 2817, 2910, 3003, 3096, 3189, 3282, 3374, 3468, 3561, 3654, 3747, 3840, 3933, 4025, 4118, 4211, 4304, 4397, 4491, 4583, 4676, 4769, 4862, 4955, 5048, 5141, 5234, 5327, 5420, 5512, 5605, 5698, 5791, 5884, 5978, 6071, 6164, 6256, 6349, 6442, 6535, 6628, 6721, 6814]
    攻击次数2 = 20
    CD = 180

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 黑曜神技能29(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 黑曜神技能30(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    学习间隔 = 2
    等级精通 = 1
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 黑曜神技能31(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((黑曜神等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

黑曜神技能列表 = []
i = 0
while i >= 0:
    try:
        exec('黑曜神技能列表.append(黑曜神技能' + str(i) + '())')
        i += 1
    except:
        i = -1

黑曜神技能序号 = dict()
for i in range(len(黑曜神技能列表)):
    黑曜神技能序号[黑曜神技能列表[i].名称] = i

黑曜神技能一觉序号 = 0
黑曜神技能二觉序号 = 0
黑曜神技能三觉序号 = 0
for i in 黑曜神技能列表:
    if i.所在等级 == 50:
        黑曜神技能一觉序号 = 黑曜神技能序号[i.名称]
    if i.所在等级 == 85:
        黑曜神技能二觉序号 = 黑曜神技能序号[i.名称]
    if i.所在等级 == 100:
        黑曜神技能三觉序号 = 黑曜神技能序号[i.名称]

黑曜神技能护石选项 = ['无']
for i in 黑曜神技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        黑曜神技能护石选项.append(i.名称)

黑曜神符文选项 = ['无','军团列阵','魔幻旋风','毁灭突进','翔空剑','碎灵屠戮','聚灵升空剑','黑暗冲击','午夜嘉年华','绚丽耀光','魔灵乱舞']

class 黑曜神角色属性(角色属性):
    实际名称 = '黑曜神'
    角色 = '守护者'
    职业 = '混沌魔灵'

    武器选项 = ['太刀', '钝器', '巨剑', '短剑']

    伤害类型选择 = ['魔法固伤']

    伤害类型 = '魔法固伤'
    防具类型 = '重甲'
    防具精通属性 = ['智力']

    主BUFF = 2

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(黑曜神技能列表)
        self.技能序号 = deepcopy(黑曜神技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        x = self.技能栏[self.技能序号['连锁共振']].TP等级
        self.技能栏[self.技能序号['魔灵召唤：波拉斯']].攻击次数 *= 1 + 0.1 * x
        self.技能栏[self.技能序号['魔灵召唤：狂暴布洛克']].攻击次数 *= 1 + 0.1 * x
        self.技能栏[self.技能序号['魔灵召唤：假面杰森']].攻击次数 *= 1 + 0.1 * x
        self.技能栏[self.技能序号['魔灵召唤：旋转小冯']].攻击次数 *= 1 + 0.1 * x
        self.技能栏[self.技能序号['魔灵召唤：迪克老爹']].攻击次数 *= 1 + 0.1 * x

        x = self.技能栏[self.技能序号['绝对魅力']].等级
        self.技能栏[self.技能序号['毁灭突进']].攻击次数2 *= 1.035 + 0.012 * x
        self.技能栏[self.技能序号['毁灭突进']].攻击次数3 *= 1.035 + 0.012 * x
        self.技能栏[self.技能序号['魔灵炸弹']].攻击次数2 *= 1.035+ 0.012 * x
        if '碎灵屠戮' in [self.护石第一栏, self.护石第二栏]:
            self.技能栏[self.技能序号['碎灵屠戮']].攻击次数1 *= 1.035 + 0.012 * x  #无碎灵屠戮护石，此条不生效
            self.技能栏[self.技能序号['绝对魅力']].描述 = '碎灵屠戮'
        else:
            self.技能栏[self.技能序号['绝对魅力']].描述 = '碎灵屠戮(部分)'
        self.技能栏[self.技能序号['碎灵屠戮']].攻击次数2 *= 1.035 + 0.012 * x

class 黑曜神(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 黑曜神角色属性()
        self.角色属性A = 黑曜神角色属性()
        self.角色属性B = 黑曜神角色属性()
        self.一觉序号 = 黑曜神技能一觉序号
        self.二觉序号 = 黑曜神技能二觉序号
        self.三觉序号 = 黑曜神技能三觉序号
        self.护石选项 = deepcopy(黑曜神技能护石选项)
        self.符文选项 = deepcopy(黑曜神符文选项)