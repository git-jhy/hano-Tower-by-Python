#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-06-06 16:24:17
# @Author  : Karl Yin (1437130953@qq.com)
# @Link    : https://blog.csdn.net/qq_41140138
# @Version : v1.0

import turtle


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# 绘制三跟柱子
def drawpoles():
    t = turtle.Turtle()
    t.hideturtle()
    t.color('gray')
    for i in range(3):
        t.up()
        t.pensize(10)
        t.speed('fast')
        t.goto(250*(i-1), 100)
        t.down()
        t.goto(250*(i-1), -100)
        t.goto(250*(i-1)-100, -100)
        t.goto(250*(i-1)+100, -100)


# 生成 plates
HEIGHT = 25
colors = ['peru', 'tomato', 'darkorange',
          'gold', 'palegreen', 'paleturquoise', 'skyblue', 'plum']

def create_plates(n):
    plates = [turtle.Turtle() for i in range(n)]
    for i in range(n):
        plates[i].speed(5)
        plates[i].hideturtle()
        c = colors[i]
        plates[i].color(c)
        plates[i].up()
        plates[i].hideturtle()
        plates[i].shape('square')
        plates[i].shapesize(1.2, 8-1.1*i)
        plates[i].goto(-250, -82 + HEIGHT*i)
        plates[i].showturtle()
    return plates

# 一次移动
def moveDisk(poles, fromPole, toPole):
    plate = poles[fromPole].pop()
    plate.goto((fromPole - 1) * 250, 120)
    plate.goto((toPole - 1) * 250, 120)
    y = poles[toPole].size() * HEIGHT - 82
    plate.goto((toPole - 1) * 250, y)
    poles[toPole].push(plate)

# 递归移动
def hano(n, poles, fromPole, withPole, toPole):
    if n == 1:
        moveDisk(poles, fromPole, toPole)
    else:
        hano(n-1, poles, fromPole, toPole, withPole)
        moveDisk(poles, fromPole, toPole)
        hano(n-1, poles, withPole, fromPole, toPole)


myscreen = turtle.Screen()
drawpoles()
plates_num = 5
plates = create_plates(plates_num)
poles = [Stack() for i in range(3)]
for plate in plates:
    poles[0].push(plate)

hano(plates_num, poles, 0, 1, 2)
turtle.done()