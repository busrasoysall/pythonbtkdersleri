"""import turtle as t

t.bgcolor("pink")
t.fillcolor("orange")
t.speed(3)

t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.done()"""


import turtle as t

t.bgcolor("skyblue")
t.speed(3)

# Kare (Ev Gövdesi)
t.penup()
t.goto(-100, -100)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Üçgen (Çatı)
t.fillcolor("brown")
t.begin_fill()
t.goto(-100, 100)
t.goto(0, 200)
t.goto(100, 100)
t.goto(-100, 100)
t.end_fill()

# Kapı
t.penup()
t.goto(-30, -100)
t.pendown()
t.fillcolor("darkred")
t.begin_fill()
for _ in range(2):
    t.forward(60)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

# Pencere
t.penup()
t.goto(50, 0)
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
for _ in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

t.hideturtle()
t.done()







