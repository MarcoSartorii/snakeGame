from collections import namedtuple
from typing import Final
GridDimensions = namedtuple("GridDimensions", "WIDTH HEIGHT")

GRID: GridDimensions = GridDimensions(16, 16)
SQUARE_SIDE: Final = 25
SQUARE_MARGIN: Final = 2
FPS: Final = 10  # suggested between 10 and 14
BACKGROUND_COLOR: Final = "Black"
SNAKE_COLOR: Final = "Lime"
HEAD_COLOR: Final = "Lime"
APPLE_COLOR: Final = "Red"
PACMAN_EFFECT: bool = True

"""
DONT MODIFY THESE
"""
WIDTH, HEIGHT = SQUARE_SIDE * GRID.WIDTH, SQUARE_SIDE * GRID.HEIGHT
