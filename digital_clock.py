# written in python 3.11.0

from turtle import Turtle, Screen
from datetime import datetime
from time import sleep

TIME_FONT = ('Verdana', 20, 'normal')
DATE_FONT = ('Arial', 20, 'normal')

screen = Screen()
screen.setup(width=200, height=150)
screen.title("Clock")
screen.tracer(0)

time_writer = Turtle()
time_writer.penup()
time_writer.hideturtle()
time_writer.speed("fastest")
time_writer.goto(0, 10)

date_writer = Turtle()
date_writer.penup()
date_writer.hideturtle()
date_writer.speed("fastest")
date_writer.goto(0, -30)

while True:
    current = datetime.now()
    current_string = str(current.replace(microsecond=0))
    current_date = current_string[:10]
    current_time = current_string[11:]
    time_writer.write(f"{current_time}", align = "center", font=TIME_FONT)
    date_writer.write(f"{current_date}", align = "center", font=DATE_FONT)
    sleep(0.1)
    screen.clear()

screen.mainloop()