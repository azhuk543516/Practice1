import turtle as trtl

# Draws a spiral
radius = 100
trtl.pendown()
for i in range(20):
  trtl.circle(radius,180)
  radius = radius - 5
trtl.penup()

""""
Draws the x and y axes beginning at the origin 100 pixels in each direction
"""
def draw_axes():
  trtl.goto(0,0)
  trtl.pendown()
  trtl.forward(100)
  trtl.backward(200)
  trtl.forward(100)
  trtl.left(90)
  trtl.forward(100)
  trtl.backward(200)
  trtl.penup()

draw_axes()