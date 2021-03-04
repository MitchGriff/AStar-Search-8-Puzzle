import copy
import time
from queue import PriorityQueue


class Puzzle:
    """A sliding-block puzzle."""
  
    def __init__(self, grid, path = ''):
        """Instances differ by their number configurations."""
        self.grid = copy.deepcopy(grid) # No aliasing!
        self.path = path
    
    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print(number, end="")
            print()
        print()

    def findLocation(self, find):
        r = 0
        for row in self.grid:
            c = 0
            for num in row:
                if num == find:
                    return r, c
                c = c + 1
            r = r + 1

    def moves(self):
        """Return a list of possible moves given the current configuration."""
        # YOU FILL THIS IN
        grid = copy.deepcopy(self.grid)
        # Get the y and x values
        [(y,x)] = [(row, column.index(' '))for row, column in enumerate(grid) if ' ' in column]

        # Create a list for moves []
        moves = []
        # Check N
        if y - 1 != -1:
            moves.append("N")
        # Check E
        if x + 1 != 3:
            moves.append("E")
        # Check S
        if y + 1 != 3:
            moves.append("S")
        # Check W
        if x - 1 != -1:
            moves.append("W")
        return moves
    
    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        # YOU FILL THIS IN
        retPuzzle = copy.deepcopy(self.grid)
        # Get the y and x values
        [(y, x)] = [(row, column.index(' ')) for row, column in enumerate(retPuzzle) if ' ' in column]

        # Make move N
        if move == "N":
            # Switch empty space and number
            retPuzzle[y][x] = retPuzzle[y-1][x]
            retPuzzle[y-1][x] = ' '
        # Make move E
        if move == "E":
            # Switch empty space and number
            retPuzzle[y][x] = retPuzzle[y][x+1]
            retPuzzle[y][x+1] = ' '
        # Make move S
        if move == "S":
            # Switch empty space and number
            retPuzzle[y][x] = retPuzzle[y+1][x]
            retPuzzle[y+1][x] = ' '
        # Make move W
        if move == "W":
            # Switch empty space and number
            retPuzzle[y][x] = retPuzzle[y][x-1]
            retPuzzle[y][x-1] = ' '
        # Return new Puzzle obj
        return Puzzle(retPuzzle, self.path + move)

    def h(self, goal):
        """Compute the distance heuristic from this instance to the goal."""
        # YOU FILL THIS IN
        # Manhattan distance
        h = 0
        for row in self.grid:
            for num in row:
                if num != ' ':
                    # Find location
                    goalLocation = goal.findLocation(num)
                    currLocation = self.findLocation(num)
                    xChange = abs(goalLocation[0] - currLocation[0])
                    yChange = abs(goalLocation[1] - currLocation[1])
                    h += xChange + yChange
        g = len(self.path)
        f = g + h
        return f

    def misplacedHeuristic(self, goal):
        """Compute the tiles that are in the wrong place for the heuristic."""
        # YOU FILL THIS IN
        # Misplaced tiles heuristic
        misplaced = 0

        for row in self.grid:
            for num in row:
                goalLocation = goal.findLocation(num)
                currLocation = self.findLocation(num)
                if goalLocation != currLocation:
                    misplaced = misplaced + 1

        return misplaced

class Agent:
    """Knows how to solve a sliding-block puzzle with A* search."""
    
    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
        # YOU FILL THIS IN
        print("HELLO ---------------------------")
        # Start the timer
        startTime = time.perf_counter()
        # Frotier priority queue
        frontier = PriorityQueue()
        # Finished list[]
        finished = []
        # Push starting puzzle onto queue
        frontier.put((puzzle.h(goal), puzzle.path, puzzle))

        while frontier.qsize() > 0:
            currentF, currentPath, currentPuzzle = frontier.get()
            currentPuzzle.display()
            if currentPuzzle.grid == goal.grid:
                returnPath = [char for char in currentPuzzle.path]
                stopTime = time.perf_counter()
                print(f"Time completed in {stopTime - startTime:0.5f} seconds")
                return returnPath
            finished.append((currentF, currentPath, currentPuzzle))
            for move in currentPuzzle.moves():
                # Check one of the moves
                tempPuzz = currentPuzzle.neighbor(move)
                # Create a tuple to be put onto the checked list
                tempTup = (tempPuzz.h(goal), tempPuzz.path, tempPuzz)
                if tempTup not in finished:
                    frontier.put(tempTup)




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
