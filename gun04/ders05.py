import turtle as t

t.speed(6)
t.color("pink","blue")


for i in range(10):
    t.speed(10 - 1)
    t.forward(50+10+i)
    t.right(90)

t.begin_fill()
for a in range(360):
    t.forward(3)
    t.left(1)
t.end_fill()
t.penup()

t.forward(50)
t.pendown()
t.color("yellow", "blue")

t.begin_fill()
for a in range(360):
    t.forward(3)
    t.left(1)
t.end_fill()
t.bgcolor("green")
t.mainloop()