from collections import namedtuple
from typing import Final
import tkinter
from Snake import Snake
from Directions import Directions
from CONSTS import BACKGROUND_COLOR, WIDTH, HEIGHT, GRID, FPS

Event = namedtuple("Event", "char")
MILLISECONDS: Final = 1000 // FPS


class Game:
    snake: Snake
    window: tkinter.Tk
    canvas: tkinter.Canvas

    def __init__(self):
        self.initGui()
        self.snake = Snake(canvas=self.canvas)
        self.initKeyBinds()

    def initGui(self):
        self.window = tkinter.Tk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.canvas = tkinter.Canvas(self.window, bg=BACKGROUND_COLOR, width=WIDTH, height=HEIGHT)
        self.window.title(f"Snake Game! {GRID.WIDTH}x{GRID.HEIGHT}")
        self.canvas.pack()

    def update(self):
        self.updateCanvas()
        self.window.after(ms=MILLISECONDS, func=self.update)

    def start(self):
        self.window.after(MILLISECONDS, self.update)
        self.window.resizable(False, False)
        self.window.mainloop()

    def updateCanvas(self):
        if not self.snake.dead:
            self.canvas.delete("all")
            self.snake.move()
            self.canvas.update()

    def initKeyBinds(self):
        self.window.bind('<KeyPress>', self.keyPressEvent)
        self.window.bind('<Left>', func=self.leftArrowPressed)
        self.window.bind('<Right>', func=self.rightArrowPressed)
        self.window.bind('<Down>', func=self.downArrowPressed)
        self.window.bind('<Up>', func=self.upArrowPressed)

    def gameOver(self):
        self.window.destroy()

    """
        I didn't want to manage the arrows this way but tkinter is weird.
        I created an Event with a char attribute so that 
        I can manually choose the event and bypass the tkinter event function
    """
    def leftArrowPressed(self, event):
        self.keyPressEvent(Event("a"))

    def rightArrowPressed(self, event):
        self.keyPressEvent(Event("d"))

    def downArrowPressed(self, event):
        self.keyPressEvent(Event("s"))

    def upArrowPressed(self, event):
        self.keyPressEvent(Event("w"))

    def keyPressEvent(self, event):
        key = event.char
        if key in ("s", "w", "a", "d"):
            if key == "s":
                self.snake.changeDirection(Directions.DOWN)
            if key == "w":
                self.snake.changeDirection(Directions.UP)
            if key == "d":
                self.snake.changeDirection(Directions.RIGHT)
            if key == "a":
                self.snake.changeDirection(Directions.LEFT)
