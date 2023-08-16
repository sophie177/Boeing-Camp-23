# Boeing Programming Camp 2023
# Python Turtle Art Demo : Day 3
# Lecture guide / activity to guide understanding of turtle


# Questions for students:  Sections are separated with comment blocks. After copy-pasting a section, look at the following parts: 
#  
# 1. What colors are named? Can you change those?
# 2. What integers are being used and where? Can you change the ones in parentheses?
#   -> example: pen.right(180)
# 3. We're using floats to represent degrees of angles. What happens when you change a float value and then press "run"? 

# First code block : A simple box. START HERE ! 
import turtle

t = turtle.Turtle()

# we can change some of these colors! But why aren't we using double-quotes? (Hint: it's because we're not using strings anymore.)
for c in ['red', 'green', 'blue', 'yellow']: 
    t.color(c)
    t.forward(75) # what happens when we change these integers? What do they determine?
    t.left(90)

# Second code block: A triangle. 
for i in range(1):
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)


# Third code block: a star! 
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

# Fourth code block: a snowflake! 
for i in range(6):
      color("pink")
      forward(100)
      left(30)
      forward(50)
      backward(50)
      right(60)
      forward(50)
      backward(50)
      left(30)
      backward(100)
      right(60)

# Last code block : a smiley face. 
import turtle

# turtle object
pen = turtle.Turtle()

# function for creation of eye
def eye(col, rad):
	pen.down()
	pen.fillcolor(col)
	pen.begin_fill()
	pen.circle(rad)
	pen.end_fill()
	pen.up()


# draw face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

# draw eyes
pen.goto(-40, 120)
eye('white', 15)
pen.goto(-37, 125)
eye('black', 5)
pen.goto(40, 120)
eye('white', 15)
pen.goto(40, 125)
eye('black', 5)

# draw nose
pen.goto(0, 75)
eye('black', 8)

# draw mouth
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()

# draw tongue
pen.goto(-10, 45)
pen.down()
pen.right(180)
pen.fillcolor('red')
pen.begin_fill()
pen.circle(10, 180)
pen.end_fill()
pen.hideturtle()




