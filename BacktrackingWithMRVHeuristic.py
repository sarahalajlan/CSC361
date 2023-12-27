class BacktrackingWithMRVHeuristic:
    def __init__(self):
        self.NoVarAssigend = 0
        self.NoConChecks = 0
        self.startTime = 0

    def BacktrackingMRV(self, grid):
        self.NoVarAssigend = 0
        self.NoConChecks = 0
        self.startTime = time.time()

        for i in range(len(grid) - 1):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    loc = [i, j]

        a = self.BacktrackingMRVRec(grid)

        print("========================")
        print("backtrack with mrv heuristic")
        print("========================")
        printTenner(grid, self.NoVarAssigend, self.NoConChecks, self.startTime, 1)
        print()
        print("========================")
        return a

    def BacktrackingMRVRec(self, grid):
        if isComplete(grid):
            return True

        MinValDomLoc = [0, 0]
        maxConstraint = 0

        for i in range(len(grid) - 1):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    count = self.CountConstraints(grid, i, j)
                    if count > maxConstraint:
                        maxConstraint = count
                        MinValDomLoc[0] = i
                        MinValDomLoc[1] = j

        for val in range(10):
            w, z = MinValDomLoc

            grid[w][z] = val
            self.NoVarAssigend += 1

            if checkConstraint(grid, w, z, grid[len(grid) - 1][z]):
                bool_val = self.BacktrackingMRVRec(grid)
                if bool_val:
                    return True
                elif val == 9:
                    grid[w][z] = -1
            else:
                grid[w][z] = -1

        return False

    def CountConstraints(self, grid, row, col):
        count = 0

        for k in range(10):
            grid[row][col] = k
            temp = self.NoConChecks
            if not checkConstraint(grid, row, col, grid[len(grid) - 1][col]):
                count += 1
            self.NoConChecks = temp
            grid[row][col] = -1

        return count
