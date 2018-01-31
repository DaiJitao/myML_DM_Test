# coding:utf-8

corpus = [
'考古 手铲 手 铲 手 铲 末端 把手 手铲 铲 刃 砍 刃 刮刃 弧形 刃 铲 刃 把手 正对 铲 刃 刃 把手 中轴线 在手 铲 投影 砍刃手 铲 把手 接续 砍刃刃 把手 中轴线 在手 铲 投影 夹角 钝角 刮刃 铲 刃 砍 刃 刮刃刃 把手 中轴线 在手 铲 投影 夹角 锐角 弧形 刃 手 铲 铲 刃 延续 把手 处 一把手 铲 多种 铲 刮 砍 弧形 刃 精细 器物 误伤',
'果园 旋耕机 农业机械 果园 自走式 微型 旋耕机 底盘 底盘 蜗杆 轴 蜗轮 变速箱 蜗轮 变速箱 蜗轮 变速箱 发动机 蜗轮 变速箱 蜗轮 轴 旋耕 刀 蜗轮 变速箱 蜗轮 轴 驱动轮 底盘 耕刀 深度 杆 底盘 端 扶手 架 扶手 果园 自走式 微型 旋耕机 结构设计 蜗轮 蜗杆 变速 目的 坚固耐用 强劲 紧凑 旋耕 大大提高 灵活 运用自如 减轻 劳动强度 扶手 扶手 架 低矮 树木 随意 扶手 耕种 增加 灵活性',
'果园 自走式 微型 旋耕机 农业机械 果园 自走式 微型 旋耕机 转台 中 柱 蜗轮 蜗杆 双箱 蜗杆 轴 转盘 转盘 柱 转盘 柱 插接 定心 圆盘 转盘 柱 插接 压板 定心 圆盘 压板 转台 转台 转台 孔 套接 柱 外围 转台 转台 轴 把手 转台 端弯片 把手 弯片 插孔 插孔 转台 孔应 插柱 果园 自走式 微型 旋耕机   转台 独立 行走 目的 '
]

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(stop_words='english')
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)

""" 计算距离 """
from sklearn.metrics.pairwise import euclidean_distances
counts = vectorizer.fit_transform(corpus).todense()
for x,y in [[0,1],[0,2],[1,2]]:
    dist = euclidean_distances(counts[x],counts[y])
    print('文档{}与文档{}的距离{}'.format(x,y,dist))