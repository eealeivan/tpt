import turtle
import math
import random

# set up screen
screen = turtle.Screen()
screen.setup(700, 700)

# draw border
border = turtle.Turtle()
border.pensize(3)
border.penup()
border.setpos(-300, -300)
border.pendown()
border_cnt = 1
while border_cnt <= 4:
    border.forward(600)
    border.left(90)
    border_cnt = border_cnt + 1

# create player
player = turtle.Turtle()
player.shape('turtle')
player.color('blue')
player.speed(0)
player.penup()

# create apples
max_apples = 5
apples = []
for i in range(max_apples):
    apple = turtle.Turtle()
    apple.shape('circle')
    apple.color('red')
    apple.penup()
    apple.speed(0)
    apple.setpos(random.randint(-300, 300), random.randint(-300, 300))
    apple.right(random.randint(0, 360))
    apples.append(apple)

speed = 1

def increase_speed():
    global speed
    speed = speed + 1

def turn_left():
    player.left(30)

def turn_right():
    player.right(30)
    
def is_in_boundaries(t):
    x = t.xcor()
    y = t.ycor()
    if x < 300 and x > -300 and y < 300 and y > -300:
        return True
    else:
        return False
        
def is_collision(t1, t2):
    d = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + 
        math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False
        
turtle.listen()
turtle.onkey(increase_speed, 'Up')
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')

while True:
    player.forward(speed)
    
    if not is_in_boundaries(player):
        player.right(180)
 
    for apple in apples:
        if is_collision(player, apple):
            apple.setpos(random.randint(-300, 300), random.randint(-300, 300))
            apple.right(random.randint(0, 360))
        else:
            apple.forward(1)

        if not is_in_boundaries(apple):
            apple.right(180)

turtle.done()
