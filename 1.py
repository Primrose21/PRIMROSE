from turtle import *
from math import *


pensize(2)

penup()

goto(-300, 300)

pendown()

setheading(180)

forward(100)

setheading(-90)

forward(150)

setheading(0)

forward(100)

penup()

rad = atan(150.0 / 2 / 100)

deg = rad * 180 / pi

left(180 - deg)

forward(100 / cos(rad))

setheading(0)

pendown()

forward(100)

mainloop()