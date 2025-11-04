import turtle, random

screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

t.goto(0, -150)
t.setheading(90)
t.color((0.4, 0.25, 0))
t.pensize(10) 

def tree(size):
    if size < 5:
        t.color("green")
        t.begin_fill()
        for _ in range(3):
            t.circle(5)
            t.right(120)
        t.end_fill()
        t.color((0.4, 0.25, 0))
        return
    t.pensize(size / 8)
    t.pendown()
    t.forward(size)
    t.left(25)
    tree(size * 0.7)
    t.right(50)
    tree(size * 0.7)
    t.left(25)
    t.backward(size)
    t.penup()

#######

def factorial(num: int) -> int:
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1
    
print(factorial(1))    
print(factorial(2))

def fib(num: int) -> int:
    if num > 2: 
        return  fib(num - 1) + (num - 2)
    else:
        return 1

print(fib(200))

# tree(90), turtle.done()




