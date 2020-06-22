import turtle
turtle.shape("turtle")
turtle.speed(1)
turtle.color("blue")
def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

counter = 0
while counter < 36:
    draw_square(150)
    turtle.right(10)
    counter += 1

turtle.exitonclick()

