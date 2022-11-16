'''
Author: 柳亦生
Date: 2022-01-13 15:40:14
LastEditors: 柳亦生
LastEditTime: 2022-11-16 23:00:44
Description: 请填写简介
ceshi 
'''


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)
    


if __name__ == "__main__":
    main()