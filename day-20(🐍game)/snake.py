from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:  # means for each in starting_position
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # position and not starting_position
        self.segment.append(new_segment)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segment[-1].position()) #to get the last position

    def move(self):
        # for seg_num in range(start=2,stop=0,spet=-1): #step is how will it go from start to stop ; going from 2 to 0 by doing -1
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()  # to get second last x
            new_y = self.segment[seg_num - 1].ycor()  # to get the second last y
            self.segment[seg_num].goto(new_x, new_y)
        # the above code will help to follow the rest of the square to the first square
        # means to tail follow the head ; where its going
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:#turtle as a heading method
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:#so that it directly don't go from up to down
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)