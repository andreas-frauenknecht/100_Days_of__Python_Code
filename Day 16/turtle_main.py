from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue", "darkgreen")
timmy.forward(100)
timmy.tilt(90)
timmy.forward(200)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()