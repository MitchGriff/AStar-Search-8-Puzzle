import copy
import time
import random
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

        tempGrid = copy.deepcopy(self.grid)
        for i in range(3):
            for j in range(3):
                if tempGrid[i][j] != goal.grid[i][j] and tempGrid[i][j] != ' ':
                    misplaced += 1

        # Add previous nodes to it
        g = len(self.path)
        misplaced += g
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
        #   Use Manhattan Distance
        frontier.put((puzzle.h(goal), puzzle.path, puzzle))
        #   Use the misplaced tiles heuristic
        #frontier.put((puzzle.misplacedHeuristic(goal), puzzle.path, puzzle))
        nodesExplored = 0
        while frontier.qsize() > 0:
            currentF, currentPath, currentPuzzle = frontier.get()
            #currentPuzzle.display()
            if currentPuzzle.grid == goal.grid:
                returnPath = [char for char in currentPuzzle.path]
                stopTime = time.perf_counter()
                print(f"Time completed in {stopTime - startTime:0.5f} seconds")
                print("Nodes Explored:", nodesExplored)
                return returnPath
            finished.append((currentF, currentPath, currentPuzzle))
            for move in currentPuzzle.moves():
                # Check one of the moves
                tempPuzz = currentPuzzle.neighbor(move)
                # Create a tuple to be put onto the checked list
                #   Use Manhattan Distance
                tempTup = (tempPuzz.h(goal), tempPuzz.path, tempPuzz)
                #   Use the misplaced tiles heuristic
                #tempTup = (tempPuzz.misplacedHeuristic(goal), tempPuzz.path, tempPuzz)
                nodesExplored += 1
                if tempTup not in finished:
                    frontier.put(tempTup)


    def randomWalk(self, puzzle, goal):
        startTime = time.perf_counter()

        counter = 0
        while (puzzle.grid != goal.grid):
            potentialMoves = []
            for move in puzzle.moves():
                potentialMoves.append(move)
            new_grid = puzzle.neighbor(random.choice(potentialMoves))
            if new_grid.grid == goal.grid:
                finishTime = time.perf_counter()
                print(f"Time completed in {finishTime - startTime:0.5f} seconds")
                print(counter)
                return list(new_grid.path)
            counter = counter + 1
            puzzle = new_grid


    def hillClimbing(self, puzzle, goal):
        neighbor = PriorityQueue()
        current = PriorityQueue()

        current.put((puzzle.h(goal), puzzle.path, puzzle))

        while not current.empty():
            currentH, currentPathLen, new_grid = current.get()

            if new_grid.grid == goal.grid:
                return list(new_grid.path)
            else:
                for move in new_grid.moves():
                    childNode = new_grid.neighbor(move)
                    neighbor.put((childNode.h(goal), childNode.path, childNode))
                neighborH, neighborPathLen, neighbor_grid = neighbor.get()
                neighbor_grid.display()
                if neighbor_grid == goal.grid or neighborH >= currentH:
                    return list(neighbor_grid.path)
                else:
                    current.put((neighbor_grid.h(goal), neighbor_grid.path, neighbor_grid))




def main():
    """Create a puzzle, solve it with A*, and console-animate."""
    
    puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
    puzzle.display()
    
    agent = Agent()
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    path = agent.astar(puzzle, goal)
    # Random walk agent call
    #path = agent.randomWalk(puzzle, goal)
    # Hill Climbing call
    #path = agent.hillClimbing(puzzle, goal)
    
    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()


if __name__ == '__main__':
    main()
