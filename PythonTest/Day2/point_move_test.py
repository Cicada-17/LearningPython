'''
Author: 柳亦生
Date: 2022-01-13 16:15:36
LastEditors: 柳亦生
LastEditTime: 2022-01-13 16:44:31
Description: 请填写简介
'''
'''
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        
        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量
        
        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
'''

from math import sqrt


class Point(object):
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def move_vertical(self, y):
        self._y += y

    def move_horizantal(self, x):
        self._x += x

    def distance(self, x, y):
        return sqrt((self._x-x)**2 + (self._y-y)**2)

    def show(self):
        return(self._x, self._y)


def main():
    a_point = Point(1, 1)
    print(a_point.distance(5, 5))


if __name__ == '__main__':
    main()
