from math import *
from PublicReference.base import *

# 2020.7.3  数据有待修整
# 2020.9.20 加入新护石，改为三觉版本

# 武器战斧
class 神启·异端审判者主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '战斧':
            return round(self.CD / self.恢复 * 1.1, 1)
            


# 战斧精通
class 神启·异端审判者技能0(被动技能):
    名称 = '战斧精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 5)
        else :
            return round(0.95 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)
        
# 一觉被动
class 神启·异端审判者技能1(被动技能):
    名称 = '异端烙印'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)


# 二觉被动
class 神启·异端审判者技能2(被动技能):
    名称 = '定罪法则'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)
    关联技能2 = ['火焰精华']#此处删除神焰
    def 加成倍率2(self, 武器类型):
        if self.等级 ==0:
            return 1.0
        else:
            return(round(1.073 + 0.017 * self.等级, 5)/ self.加成倍率(武器类型))
    冷却关联技能 = ['火焰精华','神焰']
    def CD缩减倍率(self, 武器类型):
        if  self.等级 ==0:
            return 1.0
        else:
            return 0.85

# 三觉被动
class 神启·异端审判者技能3(被动技能):
    名称 = '狂炎告解'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 惩戒十字
class 神启·异端审判者技能4(神启·异端审判者主动技能):
    名称 = '惩戒十字'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1186 + 1779 - 120 - 180
    成长 = 300
    CD = 6
    TP成长 = 0.10
    TP上限 = 5
    倍率 = round((1/1.12)*1.133,8)

# 净化火焰瓶
class 神启·异端审判者技能5(神启·异端审判者主动技能):
    名称 = '净化火焰瓶'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2938 - 298
    成长 = 298
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

# 裁决之击
class 神启·异端审判者技能6(神启·异端审判者主动技能):
    名称 = '裁决之击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 4449 - 451.5
    成长 = 451.5
    CD = 8
    TP成长 = 0.10
    TP上限 = 5
    #倍率 = 1*1.134，弃，2020年11月29日微调


# 火焰精华
class 神启·异端审判者技能7(神启·异端审判者主动技能):
    名称 = '火焰精华'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 29
    基础 = 4315 - 688
    成长 = 688
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 神焰
# 三觉版本改版，tp为基础精通
class 神启·异端审判者技能8(神启·异端审判者主动技能):
    名称 = '神焰'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    基础 = 2416*9.452#补基础精通
    成长 = 0
    CD = 10
    TP成长 = 0.10
    TP上限 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 2)
        else:
            return round(1.15 + 0.02 * (self.等级 - 10), 2)

# 审判重击
class 神启·异端审判者技能9(神启·异端审判者主动技能):
    名称 = '审判重击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2852 + 3032 - 290 - 307
    成长 = 290 + 307
    CD = 10
    TP成长 = 0.10
    TP上限 = 5
    #倍率 = round((1/1.081)*1.129,8)，弃

# 神焰斩
class 神启·异端审判者技能10(神启·异端审判者主动技能):
    名称 = '神焰斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    
    基础 = 1209  - 123 
    成长 = 123 
    攻击次数 = 1
    
    基础2 = 10903 -1106
    成长2 = 1106
    攻击次数2 = 1
   
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 = 1.29
            self.CD *= 0.85
        elif x == 1:
            self.攻击次数 = 0
            self.攻击次数2 = 1.38
            self.CD *= 0.85

# 神焰洗礼
class 神启·异端审判者技能11(神启·异端审判者主动技能):
    名称 = '神焰洗礼'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 9139 - 928#2020年11月29日微调
    成长 = 928
    CD = 15
    TP成长 = 0.10
    TP上限 = 5


# 神焰怒火
class 神启·异端审判者技能12(神启·异端审判者主动技能):
    名称 = '神焰怒火'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1


    基础 = 1670 - 169.5
    成长 = 169.5
    攻击次数 = 5

    基础2 = 5567 - 565
    成长2 = 565
    攻击次数2 = 1

    倍率 = round((1/1.127)*1.139,8)
    


    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.攻击次数 += 2
        elif x == 1:
            self.CD *= 0.85
            self.攻击次数 += 2
            self.倍率 *= 1.09

        
# 行刑
class 神启·异端审判者技能13(神启·异端审判者主动技能):
    名称 = '行刑'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 23205 -2354.5
    成长 = 2354.5
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    是否装备护石 = 0

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.是否装备护石 = 1
        elif x == 1:
            self.CD *= 0.9
            self.是否装备护石 = 2

#数据未录
# 一觉
class 神启·异端审判者技能14(神启·异端审判者主动技能):
    名称 = '火刑'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    #多段
    基础 = 10371 - 678 *12
    成长 = 678
    攻击次数 = 15 *1.1
    #前2
    基础2 = 9712 + 29135 - 12 *(633+1901)
    成长2 = 633 +1901
    攻击次数2 = 1
    

    CD = 145


# 神焰漩涡,最大旋转
class 神启·异端审判者技能15(神启·异端审判者主动技能):
    名称 = '神焰漩涡'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1


    基础 = 1635 - 166
    成长 = 166    
    攻击次数 = 9

    基础2 = 3451 - 350.16
    成长2 = 350.16
    攻击次数2 = 1

    倍率 = round((1/1.127)*1.13,8)

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 3
            self.攻击次数 *= 0.94
            self.攻击次数2 *= 1.14
        elif x == 1:
            self.攻击次数 += 3
            self.攻击次数 *= 1.01######
            self.攻击次数2 *= 1.14
        
# 净化之焰

class 神启·异端审判者技能16(神启·异端审判者主动技能):
    名称 = '净化之焰'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    
    基础 = 28032 - 2844
    成长 = 2844


    CD = 40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.27#####

# 裁决轮回斩
class 神启·异端审判者技能17(神启·异端审判者主动技能):
    名称 = '裁决轮回斩'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 2858 - 290
    成长 = 290
    攻击次数 = 3

    基础2 = 45518 - 4618
    成长2 = 4618
    攻击次数2 = 1

    CD = 40

    倍率 = round((1/1.127)*1.133,8)

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 -= 1
            self.攻击次数2 *= 1.26
            self.CD *= 0.92
            self.攻击次数 *= 1.37



# 车轮刑
class 神启·异端审判者技能18(神启·异端审判者主动技能):
    名称 = '车轮刑'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = (1872 - 190)*26 +12016 - 1219
    成长 = 190 *26 + 1219
    CD = 45

    倍率 = round((1/1.126)*1.127,8)
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.31

# 二觉
class 神启·异端审判者技能19(神启·异端审判者主动技能):
    名称 = '炎狱祭坛：炮烙'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = (33499 - 4030*5) *3 + 150746 - 18135*5
    成长 = 4030 *3 + 18135
    CD = 180
    倍率 = round((1/1.127)*1.132,8)

# 95
class 神启·异端审判者技能20(神启·异端审判者主动技能):
    名称 = '补赎逆十字'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 44324 - 4496.6
    成长 = 4496.6
    攻击次数 = 1

    基础2 = 55405 - 5620.8
    成长2 = 5620.8
    攻击次数2 = 1

    基础3 = 554 - 56.2
    成长3 = 56.2
    攻击次数3 = 20 +20

    CD = 60

# 三觉
class 神启·异端审判者技能21(神启·异端审判者主动技能):
    名称 = '无间狱·焚罪'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 37813 - 8769
    成长 = 8769
    攻击次数 = 1

    基础2 = 15125 - 3507
    成长2 = 3507
    攻击次数2 = 10

    基础3 = 189069 - 43843
    成长3 = 43843
    攻击次数3 = 1
    CD = 290
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0



神启·异端审判者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('神启·异端审判者技能列表.append(神启·异端审判者技能' + str(i) + '())')
        i += 1
    except:
        i = -1

神启·异端审判者技能序号 = dict()
for i in range(len(神启·异端审判者技能列表)):
    神启·异端审判者技能序号[神启·异端审判者技能列表[i].名称] = i

神启·异端审判者一觉序号 = 0
神启·异端审判者二觉序号 = 0
神启·异端审判者三觉序号 = 0
for i in 神启·异端审判者技能列表:
    if i.所在等级 == 50:
        神启·异端审判者一觉序号 = 神启·异端审判者技能序号[i.名称]
    if i.所在等级 == 85:
        神启·异端审判者二觉序号 = 神启·异端审判者技能序号[i.名称]
    if i.所在等级 == 100:
        神启·异端审判者三觉序号 = 神启·异端审判者技能序号[i.名称]

神启·异端审判者护石选项 = ['无']
for i in 神启·异端审判者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        神启·异端审判者护石选项.append(i.名称)

神启·异端审判者符文选项 = ['无']
for i in 神启·异端审判者技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        神启·异端审判者符文选项.append(i.名称)


class 神启·异端审判者角色属性(角色属性):
    实际名称 = '神启·异端审判者'
    角色 = '圣职者(女)'
    职业 = '异端审判者'

    武器选项 = ['战斧']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 1.93
    
    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(神启·异端审判者技能列表)
        self.技能序号 = deepcopy(神启·异端审判者技能序号)

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间) / i.等效CD(self.武器类型) + 1 + i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if '行刑' in [self.护石第一栏, self.护石第二栏, self.护石第三栏] and self.次数输入[self.技能序号['神焰']] == '/CD':
            技能释放次数[self.技能序号['神焰']] += 技能释放次数[self.技能序号['行刑']]
            
        return 技能释放次数

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['火焰精华']].被动倍率 /= self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型)
        if self.技能栏[self.技能序号['行刑']].是否装备护石 == 1:
            self.技能栏[self.技能序号['行刑']].被动倍率 /= self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型)
            self.技能栏[self.技能序号['行刑']].被动倍率 *= 1 + (self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型) - 1) * 1.39
        elif self.技能栏[self.技能序号['行刑']].是否装备护石 == 2:
            self.技能栏[self.技能序号['行刑']].被动倍率 /= self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型)
            self.技能栏[self.技能序号['行刑']].被动倍率 *= 1 + (self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型) - 1) * 2.00


class 神启·异端审判者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 神启·异端审判者角色属性()
        self.角色属性A = 神启·异端审判者角色属性()
        self.角色属性B = 神启·异端审判者角色属性()
        self.一觉序号 = 神启·异端审判者一觉序号
        self.二觉序号 = 神启·异端审判者二觉序号
        self.三觉序号 = 神启·异端审判者三觉序号
        self.护石选项 = deepcopy(神启·异端审判者护石选项)
        self.符文选项 = deepcopy(神启·异端审判者符文选项)

