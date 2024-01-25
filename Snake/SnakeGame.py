import turtle
import random
import time

delay = 0.1

# Screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

#Creating a border 
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-280,250)
turtle.pendown()
turtle.color("White")
turtle.forward(550)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(550)
turtle.right(90)
turtle.forward(500)

turtle.hideturtle()


#Score
score = 0
high_score = 0

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(0,100)

segments = []

#Scoreboard

sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score: 0  High Score: 0", align = "center", font=("ds-digital", 24, "normal"))

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#Bindings
        
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

#Main
while True: 
    screen.update()

    #To check colision with border area
    if head.xcor()>240 or head.xcor()<-260 or head.ycor()>220 or head.ycor()<-220:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide the segments of the body
        for segment in segments: 
            segment.goto(1000,1000) #Out of Range

        #Clear the Segments
        segments.clear()

        #Reset Score
        score = 0

        #Reset Delay
        delay = 0.1

        sc.clear()
        sc.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))
    

    #Check Collision with food
    if head.distance(food) < 20:
        #Move the food to random place
        x = random.randint(-280,260)
        y = random.randint(-240,240)
        food.goto(x,y)

        #Add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #Increase the score
        score += 1

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    #Move the Segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 t0 head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #Check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide Segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            #Update the score
            sc.clear()
            sc.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
