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
        return np.zeros((3, 3))

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
        """swaps the values of two tiles"""
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
        y = self.pos_row(pos)
        x = self.pos_col(pos)
        return (x, y)

    def pos_row(self, pos):
        return pos // 3

    def pos_col(self, pos):
        return pos % 3

    def find_missing_tile(self):
        return self.find_tile(0)

    def find_tile(self, val):
        for pos in range(9):
            looking_at = self.get_tile_at(pos)
            if looking_at == val:
                return pos
        return None

    def move_missing_tile(self, direction):
        pos = self.find_missing_tile()

        if direction == Direction.UP:
            if (self.pos_row(pos) == 0):
                return False
            else:
                self.swap_tiles(pos, pos - 3)
                return True
        elif direction == Direction.RIGHT:
            if (self.pos_col(pos) == 2):
                return False
            else:
                self.swap_tiles(pos, pos + 1)
                return True
        elif direction == Direction.LEFT:
            if (self.pos_col(pos) == 0):
                return False
            else:
                self.swap_tiles(pos, pos - 1)
                return True
        else:
            if (self.pos_row(pos) == 2):
                return False
            else:
                self.swap_tiles(pos, pos + 3)
                return True


def move_test():
    puzzle = Puzzle8()
    print(puzzle.move_missing_tile(Direction.RIGHT))
    print(puzzle)
    print(puzzle.move_missing_tile(Direction.RIGHT))
    print(puzzle.move_missing_tile(Direction.RIGHT))
    print(puzzle.move_missing_tile(Direction.DOWN))
    print(puzzle)

def swap_test():
    puzzle = Puzzle8()
    puzzle.swap_tiles(0, 8)
    puzzle.swap_tiles(0, 3)
    puzzle.swap_tiles(8, 4)
    print(puzzle)
    print(puzzle.find_missing_tile())
    print(puzzle.find_missing_tile() == 4)

if __name__ == "__main__":
    move_test()