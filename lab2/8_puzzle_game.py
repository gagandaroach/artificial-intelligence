"""
Artifical Intelligence - MSOE
Author - Gagan Daroach <gagandaroach@gmail.com>
April 26 2019

An implementation of the Puzzle8 Game. 
This file is part of my coursework during my undergrad at Milwaukee School of Engineering.
The purpose of this file is to be used as a illustration and learning tool
    for the hill climbing and a* search techniques with different heuristics.
"""

import numpy as np
import random
import pprint as pp
from enum import Enum, auto


class Direction(Enum):
    RIGHT = auto()
    LEFT = auto()
    DOWN = auto()
    UP = auto()


class Puzzle8:
    """
    Position Locations
    [ [0. 1. 2.]
      [3. 4. 5.]
      [6. 7. 8.] ]
    """
    def __init__(self, pattern = "012345678"):
        self.grid = self.emptyGrid()
        self.load_pattern(pattern)

    def emptyGrid(self):
        return np.zeros((3, 3))

    def load_pattern(self, pattern):
        """pattern format: 012345678"""
        if len(pattern) != 9:
            print("Error - Pattern %s was not the correct length." % pattern)
        else:
            for pos in range(9):
                self.set_tile_at(pos, pattern[pos])

    def dump_pattern(self):
        pattern = ""
        for index in range(9):
            pattern += str(int(self.get_tile_at(index)))
        return pattern

    def __str__(self):
        return ' Grid Printout:\n' + str(self.grid)

    def swap_tiles(self, pos1, pos2):
        """swaps the values of two tiles"""
        temp = self.get_tile_at(pos1)
        self.set_tile_at(pos1, self.get_tile_at(pos2))
        self.set_tile_at(pos2, temp)

    def get_tile_at(self, pos):
        coordinates = self.pos_to_coordinate(pos)
        return int(self.grid[coordinates[1]][coordinates[0]])

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

    def randomize_puzzle(self, num_random_moves = 15, debug = False):
        count = 0
        while count < num_random_moves:
            random_direction = random.choice(list(Direction))
            if (self.move_missing_tile(random_direction)):
                if debug: print(self)
                count += 1

    def calculate_misplaced_tiles(self, solution_pattern, debug = False):
        num_correct = 0
        for pos in range(9):
            if int(self.get_tile_at(pos)) == int(solution_pattern[pos]):
                if debug: print(solution_pattern[pos], self.get_tile_at(pos))
                num_correct += 1
        return 9 - num_correct

    def calculate_manhattan_distance(self, solution_pattern, debug = False):
        man_distance = 0
        for pos in range(9):
            my_tile = int(self.get_tile_at(pos))
            sol_tile = int(solution_pattern[pos])
            my_pos = self.find_tile(my_tile)
            sol_pos = self.find_tile(sol_tile)
            distance = self.pos_distance(my_pos, sol_pos)
            man_distance += distance
        return man_distance

    def pos_distance(self, pos1, pos2):
        coord1 = self.pos_to_coordinate(pos1)
        coord2 = self.pos_to_coordinate(pos2)
        deltaX = abs(coord1[0] - coord2[0])
        deltaY = abs(coord1[1] - coord2[1])
        return deltaX + deltaY

# end of class, start of my tests
# used during development to see if stuff was working right

def calculate_manhattan_distance_test():
    puzzle = Puzzle8()
    print('should be 0: ', puzzle.calculate_manhattan_distance("012345678", True))
    print('should be something: ', puzzle.calculate_manhattan_distance("876543210", True))
    print('should be something smaller; ', puzzle.calculate_manhattan_distance("012348765", True))

def calculate_misplaced_tiles_test():
    puzzle = Puzzle8()
    print('should be 0: ', puzzle.calculate_misplaced_tiles("012345678", True))
    print('should be 8: ', puzzle.calculate_misplaced_tiles("876543210", True))
    print('should be half; ', puzzle.calculate_misplaced_tiles("012348765", True))


def dump_pattern_test():
    puzzle = Puzzle8()
    print(puzzle.dump_pattern(), True)

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

def load_pattern_test():
    puzzle = Puzzle8()
    pattern = "158764302"
    puzzle.load_pattern(pattern)
    print(pattern, puzzle)

def randomize_test():
    puzzle = Puzzle8()
    puzzle.randomize_puzzle()
    print(puzzle)

if __name__ == "__main__":
    calculate_manhattan_distance_test()