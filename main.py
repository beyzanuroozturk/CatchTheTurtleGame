import turtle
import random

game_screen = turtle.Screen()
game_screen.bgcolor("light blue")
game_screen.title("Catch The Turtle")
FONT = ("Arial", 18, "normal")
score = 0
game_over = False

#turtle list
turtle_list=[]

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle=turtle.Turtle()


def score_setup_turtle():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("dark blue")

    top_height = game_screen.window_height()/2
    y=top_height * 0.9
    score_turtle.goto(0,y)
    score_turtle.write("Score:0", move=False, align="center", font=FONT)



grid_size=10

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write("Score:{}".format(score), move=False, align="center", font=FONT)




    t.onclick(handle_click)
    t.penup()
    t.color("green")
    t.shape("turtle")
    t.shapesize(2,2)
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)




x_coordinates=[-20,-10,0,10,20]
y_coordinates=[20,10,0,-10]
def turtle_setup():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        game_screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.color("dark blue")

    top_height = game_screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.goto(0, y-30)
    countdown_turtle.clear()
    if time >0:
        countdown_turtle.clear()
        countdown_turtle.write("time:{}".format(time), move=False, align="center", font=FONT)
        game_screen.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write("Game Over!", move=False, align="center", font=FONT)
        hide_turtles()


turtle.tracer(0)

score_setup_turtle()
turtle_setup()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)

turtle.mainloop()
