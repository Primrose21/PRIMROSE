from turtle import*
from math import*

pensize(3)
"""
我
画了个正方形
宽为100
它
又大又宽
"""
penup()
goto(-100,100)

pendown()
for j in range(3):
    for i in range(4):
        right(90)
        forward(100)

    penup()
    forward(110)
    pendown()

mainloop()