'''
Author: 柳亦生
Date: 2021-12-14 16:56:08
LastEditors: 柳亦生
LastEditTime: 2021-12-19 16:05:24
Description: 请填写简介
'''
#  is palindrome


def is_palindrome(num):
    temporary = num
    p = 0
    while temporary > 0:
        p = p * 10 + temporary % 10
        temporary //= 10
    return p == num


def is_prime(num):
    for factor in range(2, int(num ** 0.5)+1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':
    num = int(input('Input postive integer :'))
    if is_palindrome(num) and is_prime(num):
        print('%d is palindrome prime' % num)


def main():
    pass
