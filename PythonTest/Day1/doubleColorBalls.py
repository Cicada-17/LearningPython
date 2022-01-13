'''
Author: 柳亦生
Date: 2021-12-18 03:27:31
LastEditors: 柳亦生
LastEditTime: 2022-01-11 16:55:20
Description: 请填写简介
'''
import random


def random_select():
    red_balls = [x for x in range(1, 34)]
    select_balls = []
    select_balls = random.sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(random.randint(1, 16))
    return select_balls


def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end='')
        print(f'{ball}', end=' ')


def main():
    print(random_select())
    display(random_select())


if __name__ == '__main__':
    main()
