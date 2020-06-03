import turtle 

size = int(input('enter the size of your house(max: 100): '))
if size > 100:
    size = 100
elif size < 0:
    size = 1

screen = turtle.getscreen()
t = turtle.Turtle()


t.speed(10000)


for i in range(4):
    t.forward(size)
    t.left(90)

t.penup
t.left(90)
t.forward(size)
t.right(30)

for i in range(3):
    t.forward(size)
    t.right(120)

t.left(30)
t.right(180)
t.forward(size)
t.left(90)

t.forward(size // 2)

for i in range(4):
    t.forward(size // 4)
    t.left(90)



screen.mainloop()
