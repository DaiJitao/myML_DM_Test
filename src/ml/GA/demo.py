# -*-coding:utf-8 -*-
# 目标求解2*sin(x)+cos(x)最大值
import random
import math
import matplotlib.pyplot as plt


# 初始化生成chromosome_length大小的population_size个个体的二进制基因型种群
def species_origin(population_size, chromosome_length):
    """
    种群初始化
    :param population_size: 种群的数量
    :param chromosome_length: 染色体（个体）大小
    :return:
    """
    population = [[]]
    # 二维列表，包含染色体和基因
    for i in range(population_size):
        temporary = []
        # 染色体暂存器
        for j in range(chromosome_length):
            temporary.append(random.randint(0, 1))
            # 随机产生一个染色体,由二进制数组成
        population.append(temporary)
        # 将染色体添加到种群中
    return population[1:]
    # 将种群返回，种群是个二维数组，个体和染色体两维

data = species_origin(20, 6)
print("data: ", data)


def translation(population, chromosome_length):
    """
    #从二进制到十进制
    input:种群,染色体长度
    :param population: lst [[1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0]]
    :param chromosome_length:  int 染色体（个体）大小
    :return:
    """
    temporary = []
    for i in range(len(population)):
        total = 0
        for j in range(chromosome_length):
            total += population[i][j] * (math.pow(2, j))
            # 从第一个基因开始，每位对2求幂，再求和
            # 如：0101 转成十进制为：1 * 20 + 0 * 21 + 1 * 22 + 0 * 23 = 1 + 0 + 4 + 0 = 5
        temporary.append(total)
        # 一个染色体编码完成，由一个二进制数编码为一个十进制数
    return temporary
    # 返回种群中所有个体编码完成后的十进制数

print(translation(data, 6))