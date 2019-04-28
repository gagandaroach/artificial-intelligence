"""
Artifical Intelligence - MSOE
Gagan Daroach
April 26 2019
"""

import numpy as np
import pprint as pp
from enum import Enum

class Position(Enum):
    0
    1
    2
    3
    4
    5
    6
    7
    8

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
        temp = 0

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