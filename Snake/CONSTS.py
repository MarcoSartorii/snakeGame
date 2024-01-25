from collections import namedtuple
from typing import Final
GridDimensions = namedtuple("GridDimensions", "WIDTH HEIGHT")

GRID: GridDimensions = GridDimensions(30, 30)
side: Final = 20
MARGIN: Final = 2
FPS: Final = 8
BACKGROUND_COLOR: Final = "black"
SNAKE_COLOR: Final = "Blue"
APPLE_COLOR: Final = "red"
PACMAN_EFFECT: bool = False

"""
DONT MODIFY THESE
"""
WIDTH, HEIGHT = side * GRID[0], side * GRID[1]
