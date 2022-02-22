import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
## Race 1
michMove = random.randint(1,101)
leoMove = random.randint(1,101)
michelangelo.forward(michMove)
leonardo.forward(leoMove)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## Race 2
for x in range(0,10):
  michMove = random.randint(0,11)
  leoMove = random.randint(0,11)
  michelangelo.forward(michMove)
  leonardo.forward(leoMove)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
michelangelo.down()
for x in range (3,13):
  if x == 3 or x == 4 or x == 6 or x==9 or x==12:
    for y in range (0,x):
      angle = 360/x
      michelangelo.color('orange')
      michelangelo.forward(angle)
      michelangelo.right(angle)
    michelangelo.clear()
  
window.exitonclick()
