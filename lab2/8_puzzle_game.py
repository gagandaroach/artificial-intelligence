"""
Artifical Intelligence - MSOE
Gagan Daroach
April 26 2019
"""

import numpy as np
import pprint as pp
from enum import Enum, auto

class Direction(Enum):
    RIGHT = auto()
    LEFT = auto()
    DOWN = auto()
    UP = auto()

class Puzzle8:

    def __init__(self):
      self.grid = self.emptyGrid()
      self.initialize_grid(self.grid)

    def emptyGrid(self):
        return np.zeros((3,3))

    def initialize_grid(self, grid):
        """
        [ [0. 1. 2.] 
          [3. 4. 5.] 
          [6. 7. 8.] ]
        """
        # count = 0
        # for y in range(0,3):
        #     for x in range(0,3):
        #         grid[y][x] = count
        #         count += 1
        for pos in range(9):
            self.set_tile_at(pos, pos)
    
    def __str__(self):
        return ' Grid Printout:\n' + str(self.grid)

    def swap_tiles(self, pos1, pos2):
        """swaps the location of two tiles"""
        temp = self.get_tile_at(pos1)
        self.set_tile_at(pos1, self.get_tile_at(pos2))
        self.set_tile_at(pos2, temp)

    def get_tile_at(self, pos):
        coordinates = self.pos_to_coordinate(pos)
        return self.grid[coordinates[1]][coordinates[0]]

    def set_tile_at(self, pos, val):
        coordinates = self.pos_to_coordinate(pos)
        self.grid[coordinates[1]][coordinates[0]] = val

    def pos_to_coordinate(self, pos):
        y = pos // 3
        x = pos % 3
        return (x,y)

if __name__ == "__main__":
    puzzle = Puzzle8()
    print(puzzle)
    puzzle.swap_tiles(0, 8)
    puzzle.swap_tiles(0, 3)

    print(puzzle)