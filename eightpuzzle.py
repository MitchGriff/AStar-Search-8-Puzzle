import copy
import time


class Puzzle:
    """A sliding-block puzzle."""
  
    def __init__(self, grid):
        """Instances differ by their number configurations."""
        self.grid = copy.deepcopy(grid) # No aliasing!
    
    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print(number, end="")
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current configuration."""
        # YOU FILL THIS IN
    
    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        # YOU FILL THIS IN

    def h(self, goal):
        """Compute the distance heuristic from this instance to the goal."""
        # YOU FILL THIS IN


class Agent:
    """Knows how to solve a sliding-block puzzle with A* search."""
    
    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
        # YOU FILL THIS IN


def main():
    """Create a puzzle, solve it with A*, and console-animate."""
    
    puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
    puzzle.display()
    
    agent = Agent()
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    path = agent.astar(puzzle, goal)
    
    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()


if __name__ == '__main__':
    main()