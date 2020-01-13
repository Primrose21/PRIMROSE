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
goto(100,100)

pendown()
setheading(-90)
forward(100)

setheading(-180)
forward(100)

setheading(90)
forward(100)

setheading(0)
forward(100)

mainloop()