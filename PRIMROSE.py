from turtle import*
from math import*

#笔的粗细
pensize(3)

#画P的竖
penup()
goto(-300,100)

pendown()
setheading(-95)
forward(100)

#画P的右边部分
penup()
goto(-304,104)

pendown()
setheading(-40)
forward(45)
setheading(-150)
forward(43)

#画R的竖
penup()
goto(-250,100)

pendown()
setheading(-95)
forward(100)

#画R的右边半圆
penup()
goto(-250,100)

pendown()
setheading(-40)
forward(48)
setheading(-150)
forward(43)

#画R的最后一撇
penup()
goto(-250,50)

pendown()
setheading(-54)
forward(70)

#画I的最上面的横
penup()
goto(-200,70)

pendown()
setheading(30)
forward(40)

#画I的最下面的横
penup()
goto(-200,0)

pendown()
setheading(30)
forward(40)

#画I的竖
penup()
goto(-180,80)

pendown()
setheading(-90)
forward(70)

#画M的第一个竖
penup()
goto(-150,0)

pendown()
setheading(70)
forward(90)

#画M的第二个竖
penup()
goto(-125,0)

pendown()
setheading(70)
forward(80)

#画M的第一个捺
penup()
goto(-128,75)

pendown()
setheading(-75)
forward(50)

#画M的第二个捺
penup()
goto(-104,70)

pendown()
setheading(-75)
forward(80)

#画R的竖
penup()
goto(-60,95)

pendown()
setheading(-95)
forward(100)

#画R的右边半圆部分
penup()
goto(-60,95)

pendown()
setheading(-40)
forward(45)
setheading(-150)
forward(43)

#画R的最后一撇
penup()
goto(-65,50)

pendown()
setheading(-54)
forward(70)

#画O 是菱形哦
penup()
goto(10, 90)

pendown()
setheading(-120)
forward(50)

setheading(-60)
forward(50)

setheading(60)
forward(50)

setheading(120)
forward(50)

#画S 闪电形
penup()
goto(70, 90)

pendown()
setheading(-120)
forward(40)

setheading(-60)
forward(50)

setheading(-120)
forward(35)

#画e的左边弯折部分
penup()
goto(117, 90)

pendown()
setheading(-113)
forward(50)
setheading(-68)
forward(68)

#画e的右边弯折部分
penup()
goto(117, 90)

pendown()
setheading(-65)
forward(40)
setheading(-136)
forward(47)

mainloop()