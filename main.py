import turtle as trtl

# Draws a spiral
radius = 100
trtl.pendown()
for i in range(20):
  trtl.circle(radius,180)
  radius = radius - 5
trtl.penup