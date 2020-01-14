from turtle import*
from math import*


pensize(3)

penup()
goto(-200,100)

pendown()
 
for c in range(3):
    for i in range(3):
        for j in range(4):
            right(90)
            forward(100)

        penup()
        forward(100)
        pendown()

    penup()
    right(90)
    forward(200*c)
    right(90)
    forward(200)
    pendown()


mainloop()