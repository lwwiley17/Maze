import random
import turtle

class Maze():
    def __init__(self):
        self.screen = turtle.Screen()
        self.turtle = turtle.Turtle()
        #screen
        self.screen.screensize(400,400)
        self.screen.bgcolor("blue")
        self.screen.register_shape("custom",((10,10),(-10,10),(-10,-10),(10,-10))) #20x20 turtle
        #turtle
        self.turtle.shape("custom")
        self.turtle.color('white')
        self.turtle.penup()
        self.turtle.goto(-190,190)
        #matrix
        self.matrix = [[1 for i in range(20)] for i in range(20)]
        self.matrix[0][0] = 0
