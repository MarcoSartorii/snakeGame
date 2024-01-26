import math
import tkinter

from CONSTS import SQUARE_SIDE, SNAKE_COLOR, GRID, PACMAN_EFFECT, APPLE_COLOR, HEAD_COLOR, \
    SQUARE_MARGIN
from collections import namedtuple
from random import randint
from Directions import Directions

Coordinates = namedtuple("Coords", "x y")


class Snake:
    direction: Directions
    head: Coordinates
    apple: Coordinates
    canvas: tkinter.Canvas
    score: int
    tail: list[Coordinates]
    dead: bool

    def __init__(self, x: int = GRID.WIDTH // 2, y: int = GRID.HEIGHT // 2, canvas: tkinter.Canvas = None):
        if canvas is None:
            raise Exception("SNAKE'S CANVAS NONE")
        self.score = 0
        self.dead = False
        self.test = 1
        self.canvas = canvas
        self.head = Coordinates(x, y)
        self.tail = []
        self.spawnNewApple()
        self.direction = Directions.UP
        self.draw()

    def move(self):
        if self.dead:
            return
        newX, newY = self.head.x, self.head.y
        if self.direction in (Directions.UP, Directions.DOWN):
            newY = self.head.y - 1 if self.direction == Directions.UP else self.head.y + 1
        if self.direction in (Directions.RIGHT, Directions.LEFT):
            newX = self.head.x + 1 if self.direction == Directions.RIGHT else self.head.x - 1

        newX, newY = self.isSnakeHittingTheWall(newX, newY)

        self.moveTail()
        self.head = Coordinates(newX, newY)

        if self.head in self.tail[1:]:
            self.draw()
            self.dead = True
            return

        if self.head == self.apple:
            self.eat()

        self.draw()

    def changeDirection(self, newDirection: Directions):
        if self.isValidDirection(self.direction, newDirection):
            self.direction = newDirection

    def isSnakeHittingTheWall(self, newX: int, newY):
        isY = self.direction in (Directions.UP, Directions.DOWN)
        extremes = range(0, GRID.HEIGHT if isY else GRID.WIDTH)
        if isY:
            if newY in extremes:
                return newX, newY
        else:
            if newX in extremes:
                return newX, newY

        if not PACMAN_EFFECT:
            self.dead = True
            return (newX, newY) if isY else (newX, newY)

        if newX < 0 or newY < 0:

            return (newX, extremes[-1] - 1) if isY else (extremes[-1], newY)
        else:
            return (newX, -1) if isY else (-1, newY)

    def eat(self):
        self.score += 1
        if self.score == (GRID.WIDTH * GRID.HEIGHT) - 1:
            self.dead = True
            return
        self.spawnNewApple()
        self.tail.append(Coordinates(self.head.x, self.head.y))

    def spawnNewApple(self):
        while True:
            x = randint(0, GRID.WIDTH - 1)
            y = randint(0, GRID.HEIGHT - 1)
            if Coordinates(x, y) not in (self.head, self.tail):
                apple = Coordinates(x, y)
                break
        self.apple = apple

    def draw(self):
        for coord in self.tail:
            self.drawSquare(coord, SNAKE_COLOR)
        self.drawSquare(self.head, HEAD_COLOR)
        self.drawSquare(self.apple, APPLE_COLOR)

    def drawSquare(self, coords: Coordinates, color: str, margin=SQUARE_MARGIN):
        self.canvas.create_rectangle(
            self.getPixels(
                coords.x, coords.y, coords.x + 1, coords.y + 1, margin=margin
            ),
            fill=color, outline="")

    def moveTail(self):
        self.tail.insert(0, self.head)
        self.tail.pop()

    @staticmethod
    def getPixels(*args, margin=0) -> tuple:
        tupleCoords = tuple(args)
        argc = len(tupleCoords)
        pixels = []
        for index, coord in enumerate(tupleCoords):
            pixelPoint = coord * SQUARE_SIDE
            if index < argc // 2:
                pixelPoint += margin
            else:
                pixelPoint -= margin
            pixels.append(pixelPoint)
        return tuple(pixels)

    @staticmethod
    def isValidDirection(currentDirection: Directions, newDirection: Directions):
        if currentDirection == newDirection:
            return False
        if (Directions.UP in (currentDirection, newDirection) and
                Directions.DOWN in (currentDirection, newDirection)):
            return False
        if (Directions.LEFT in (currentDirection, newDirection) and
                Directions.RIGHT in (currentDirection, newDirection)):
            return False
        return True
