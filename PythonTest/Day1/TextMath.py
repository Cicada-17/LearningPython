'''
Author: 柳亦生
Date: 2021-12-14 16:56:08
LastEditors: 柳亦生
LastEditTime: 2021-12-17 17:04:38
Description: 请填写简介
'''
# C排列组合计算
def factorial(num):
    # 求阶乘
    result = 1
    for n in range(1,num+1):
        result *= n
    return result


