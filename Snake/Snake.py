import tkinter

from CONSTS import side, SNAKE_COLOR, GRID, PACMAN_EFFECT, APPLE_COLOR
from collections import namedtuple
from random import randint
from Directions import Direction

Coordinates = namedtuple("Coords", "x y")
ChessBoard = namedtuple("Coords", "width height")


class Snake:
    direction: Direction
    head: Coordinates
    apple: Coordinates
    canvas: tkinter.Canvas
    score: int
    dead: bool

    def __init__(self, x: int = GRID.WIDTH // 2, y: int = GRID.HEIGHT // 2, canvas: tkinter.Canvas = None):
        self.score = 0
        self.dead = False
        self.test = 1
        if canvas is None:
            raise Exception("SNAKE'S CANVAS NONE")
        self.canvas = canvas
        self.head = Coordinates(x, y)
        self.spawnNewApple()
        self.drawSnakeHead()
        self.direction = Direction.UP


    def changeDirection(self, newDirection: Direction):
        if self.isValidDirection(self.direction, newDirection):
            self.direction = newDirection

    def drawSnakeHead(self):
        self.canvas.create_rectangle(
            self.getPixels(
                self.head.x, self.head.y, self.head.x + 1, self.head.y + 1, margin=2
            ),
            fill=SNAKE_COLOR, outline="")

    def move(self):
        # todo this is my Artificial Intelligence for now
        """
        if self.apple.x > self.head.x:
            self.direction = Direction.RIGHT
       if self.apple.x < self.head.x:
            self.direction = Direction.LEFT
        if self.apple.y > self.head.y:
            self.direction = Direction.DOWN
        if self.apple.y < self.head.y:
            self.direction = Direction.UP
        """

        if self.direction == Direction.UP:
            newY = self.head.y - 1
            if not self.isSnakeHittingTheWall(newY):
                self.head = self.head._replace(y=self.head.y - 1)
        if self.direction == Direction.DOWN:
            newY = self.head.y + 1
            if not self.isSnakeHittingTheWall(newY):
                self.head = self.head._replace(y=newY)
        if self.direction == Direction.RIGHT:
            newX = self.head.x + 1
            if not self.isSnakeHittingTheWall(newX):
                self.head = self.head._replace(x=newX)
        if self.direction == Direction.LEFT:
            newX = self.head.x - 1
            if not self.isSnakeHittingTheWall(newX):
                self.head = self.head._replace(x=newX)

        if self.head == self.apple:
            self.eat()

        # TODO move tail but tail does not exist yet.
        # TODO unlucky
        self.drawSnakeHead()
        self.drawApple()

    def play(self):
        print(self.head.x)

    def drawApple(self):
        self.canvas.create_rectangle(
            self.getPixels(
                self.apple.x, self.apple.y, self.apple.x + 1, self.apple.y + 1, margin=2
            ),
            fill=APPLE_COLOR, outline="")
        pass

    @staticmethod
    def getPixels(*args, margin=0) -> tuple:
        tupleCoords = tuple(args)
        argc = len(tupleCoords)
        pixels = []
        for index, coord in enumerate(tupleCoords):
            pixelPoint = coord * side
            if index < argc // 2:
                pixelPoint += margin
            else:
                pixelPoint -= margin
            pixels.append(pixelPoint)
        return tuple(pixels)

    @staticmethod
    def isValidDirection(currentDirection: Direction, newDirection: Direction):
        if currentDirection == newDirection:
            return False
        if (Direction.UP in (currentDirection, newDirection) and
                Direction.DOWN in (currentDirection, newDirection)):
            return False
        if (Direction.LEFT in (currentDirection, newDirection) and
                Direction.RIGHT in (currentDirection, newDirection)):
            return False
        return True

    def isSnakeHittingTheWall(self, point):
        isY = False
        if self.direction in (Direction.UP, Direction.DOWN):
            isY = True

        extremes = range(0, GRID.HEIGHT if isY else GRID.WIDTH)
        if point in extremes:
            return False

        if not PACMAN_EFFECT:
            self.dead = True
            return True

        if point < 0:
            if isY:
                self.head = self.head._replace(y=extremes[-1])
                return True
            else:
                self.head = self.head._replace(x=extremes[-1])
                return True
        else:
            if isY:
                self.head = self.head._replace(y=extremes[0] - 1)
                return True
            else:
                self.head = self.head._replace(x=extremes[0] - 1)
                return True

    def eat(self):
        self.score += 1
        self.spawnNewApple()

    def spawnNewApple(self):
        while True:
            x = randint(0, GRID.WIDTH - 1)
            y = randint(0, GRID.HEIGHT - 1)
            apple = Coordinates(x, y)
            if apple != self.head:
                break
        self.apple = apple
