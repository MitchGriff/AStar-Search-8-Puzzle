from eightpuzzle import *


class Puzzles():
    puzzle_goal = [[' ', 1, 2], [3, 4, 5], [6, 7, 8]]
    puzzle1_start = [[1, 2, 5], [4, 8, 7], [3, 6, ' ']]
    puzzle2_start = [[1, 2, 5], [3, 6, ' '], [4, 8, 7]]
    puzzle3_start = [[1, 3, 2], [4, 6, 5], [' ', 7, 8]]


def test_moves1():
    result = Puzzle(Puzzles().puzzle1_start).moves()
    gold = ["N", "W"]
    assert set(gold) == set(result)
    assert len(gold) == len(result)


def test_moves2():
    result = Puzzle(Puzzles().puzzle_goal).moves()
    gold = ["E", "S"]
    assert set(gold) == set(result)
    assert len(gold) == len(result)


def test_moves3():
    result = Puzzle(Puzzles().puzzle2_start).moves()
    gold = ["N","W","S"]
    assert set(gold) == set(result)
    assert len(gold) == len(result)


def test_neighbor1():
    p = Puzzle(Puzzles().puzzle1_start).neighbor("N")
    assert [[1, 2, 5], [4, 8, ' '], [3, 6, 7]] == p.grid


def test_neighbor2():
    p = Puzzle(Puzzles().puzzle2_start).neighbor("N")
    assert [[1, 2, ' '], [3, 6, 5], [4, 8, 7]] == p.grid

def test_neighbor3():
    p = Puzzle(Puzzles().puzzle3_start).neighbor("E")
    assert [[1, 3, 2], [4, 6, 5], [7, ' ', 8]] == p.grid


def test_astar1():
    movelist = Agent().astar(Puzzle(Puzzles().puzzle1_start),Puzzle(Puzzles().puzzle_goal))
    assert ['N', 'W', 'W', 'S', 'E', 'E', 'N', 'N', 'W', 'W'] == movelist


def test_astar2():
    movelist = Agent().astar(Puzzle(Puzzles().puzzle2_start),Puzzle(Puzzles().puzzle_goal))
    assert ['S', 'W', 'N', 'E', 'N', 'W', 'W', 'S', 'S', 'E', 'N', 'W', 'N'] == movelist


def test_astar3():
    movelist = Agent().astar(Puzzle(Puzzles().puzzle3_start),Puzzle(Puzzles().puzzle_goal))
    assert ['N', 'E', 'N', 'E', 'S', 'S', 'W', 'W', 'N', 'E', 'S', 'E', 'N', 'N', 'W', 'W'] == movelist
