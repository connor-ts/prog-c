# Turtle artist
# connor ter stege
# nov 3/25

import turtle as t # this is js simpler than writing a whole line to do the same thing
import random

# whole bun of setup stuff that just makes the background blue 
screen = t.Screen()
screen.setup(800, 600) 
screen.bgcolor("skyblue")
t.hideturtle()
t.speed(0)

# the grass on the bottom for the ground

t.penup()
t.goto(-400, -150)
t.pendown()
t.color("forestgreen") # ground color
t.begin_fill()
for w in range(2): 
    t.forward(800)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()

# tree function

def tree(branch):
    if branch < 10: 
        t.color("forestgreen") # leaves color
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        return 
    t.color("saddlebrown")
    t.pensize(branch / 10)
    t.forward(branch)
    t.right(25)
    tree(branch - random.randint(10, 15))
    t.left(50)
    tree(branch - random.randint(10, 15))
    t.right(25)
    t.backward(branch)

def treeplacing(x, y):  # placing the tree equal to the screen on both sides
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    tree(70) 

# scatter grass and flowers
# i couldnt really find a way to make the grass pop so i just 
def flowers_grass(): 
    for w in range(80):
        x = random.randint(-380, 380)
        y = random.randint(-280, -160)
        t.penup()
        t.goto(x, y)
        if random.random() < 0.2:
            t.dot(6, random.choice(["red", "yellow", "purple", "pink"]))
        else:
            t.dot(4, "limegreen")

# cloud section

def drawclouds(x, y): # function which draws the clouds which the next function will place
    t.penup()
    t.color("white") # cloud color
    for w in range(random.randint(5, 7)): # randomly draw them so they look unique
        offset_x = random.randint(-25, 25)
        offset_y = random.randint(-10, 10)
        t.goto(x + offset_x, y + offset_y) # orients the circles so its not just a blob of white circles
        t.begin_fill()
        t.circle(random.randint(15, 25)) # size of the circles 
        t.end_fill()

def clouds(): 
    cloud_count = random.randint(7, 9)
    spacing = 100  # distance between clouds
    firstcloud = -350 # first cloud will always be here

    # controls what pattern the clouds are generated it
    for w in range(cloud_count):
        x = firstcloud + w * spacing + random.randint(-30, 30)
        y = random.randint(120, 250)
        drawclouds(x, y)

# draw everything/finalize where stuff is
flowers_grass()
treeplacing(-200, -150)
treeplacing(200, -150)
clouds()

t.done()
