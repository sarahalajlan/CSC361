class SimpleBacktracking:
    def __init__(self):
        self.NoVarAssigend = 0
        self.NoConChecks = 0
        self.startTime = 0
        self.nextSelections = []

    def SimpleBacktrackingSearch(self, grid):
        self.NoVarAssigend = 0
        self.NoConChecks = 0
        self.startTime = time.time()
        self.nextSelections = []

        for i in range(len(grid) - 1):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    loc = [i, j]
                    self.nextSelections.append(loc)

        a = self.SimpleBacktrackingRec(grid)

        print("========================")
        print("simple backtrack search:")
        print("========================\n")
        printTenner(grid, self.NoVarAssigend, self.NoConChecks, self.startTime, 1)
        print()
        print("========================\n")
        return a

    def SimpleBacktrackingRec(self, grid):
        if isComplete(grid):
            return True

        k = self.nextSelections[0]

        for j in range(10):
            grid[k[0]][k[1]] = j
            self.NoVarAssigend += 1

            if j == 0:
                self.nextSelections.pop(0)

            if checkConstraint(grid, k[0], k[1], grid[len(grid) - 1][k[1]]):
                if self.SimpleBacktrackingRec(grid):
                    return True
                elif j == 9:
                    grid[k[0]][k[1]] = -1
                    self.nextSelections.insert(0, k)
            else:
                if j == 9:
                    self.nextSelections.insert(0, k)
                grid[k[0]][k[1]] = -1

        return False
