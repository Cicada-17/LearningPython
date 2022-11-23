'''
Author: 柳亦生
Date: 2022-11-21 15:22:39
LastEditors: 柳亦生
LastEditTime: 2022-11-22 20:12:33
Description: 请填写简介
'''

def kelly(bet,p):
    return (bet * p -(1-p))/bet

def main():
    bellet = float(input('输入总金额!\n'))
    f = bellet*kelly(float(input('赔率：')),float(input('胜率:')))
    print(f)
    
if __name__ == '__main__':
    main()