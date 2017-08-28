import turtle
import math


def polygon(t, length, n):
    t = turtle.Turtle()
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def bob():
    bob


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n

    polygon(t, length, n)

# circle(bob,20)


def circle1(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 5
    length = circumference / n
    polygon(t, length, n)


circle1(bob, 40)
