'''
Author: 柳亦生
Date: 2022-01-11 17:00:59
LastEditors: 柳亦生
LastEditTime: 2022-01-11 17:20:06
Description: 请填写简介
'''


def josephuloop():
    persons = True * 30
    index, number, counter = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30


def main():
    pass


if __name__ == '__main__':
    main()
