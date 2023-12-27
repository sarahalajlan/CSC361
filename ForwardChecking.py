class ForwardChecking:
    def __init__(self):
        self.NoVarAssigend = 0
        self.NoConChecks = 0
        self.startTime = 0
        self.nextSelections = []

    def ForwardCheckingSearch(self, grid):
        self.NoVarAssigend = 0
        self.NoConChecks = 0
        self.startTime = time.time()
        self.nextSelections = []

        for i in range(len(grid) - 1):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    cellnum = [i, j]
                    self.nextSelections.append(cellnum)

        for i in range(len(grid) - 1):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    loc = [i, j]
                    domain = list(range(10))
                    variable = [loc, domain]
                    self.nextSelections.append(variable)

        a = self.ForwardCheckingRec(grid)

        print("========================")
        print("forward check")
        print("========================\n")
        printTenner(grid, self.NoVarAssigend, self.NoConChecks, self.startTime, 1)
        print()
        print("========================\n")
        return a

    def ForwardCheckingRec(self, grid):
        if isComplete(grid):
            return True

        n = self.nextSelections.pop(0)

        for val in range(10):
            dom = n[1]
            if val not in dom:
                if val == 9:
                    grid[n[0][0]][n[0][1]] = -1
                    self.nextSelections.append(n)
                continue

            grid[n[0][0]][n[0][1]] = val
            self.NoVarAssigend += 1

            if checkConstraint(grid, n[0][0], n[0][1], grid[len(grid) - 1][n[0][1]]):
                temp = self.forwardCheck(grid, n[0][0], n[0][1])
                bool_val = self.ForwardCheckingRec(grid)
                if bool_val:
                    return True
                elif val == 9:
                    self.nextSelections.append(n)
                    grid[n[0][0]][n[0][1]] = -1

                for e in temp:
                    try:
                        DomSearch = self.searchDomain(e[0][0], e[0][1])
                        for p in range(len(e[1])):
                            if e[1][p] != -1:
                                DomSearch[e[1][p]] = e[1][p]
                    except Exception as x:
                        pass
            else:
                if val == 9:
                    grid[n[0][0]][n[0][1]] = -1
                    self.nextSelections.append(n)

        return False

    def searchDomain(self, rowNum, colNum):
        for k in self.nextSelections:
            if k[0][0] == rowNum and k[0][1] == colNum:
                return k[1]
        return None

    def AdjecentReduction(self, grid, rowNum, colNum, removedDomain):
        for i in range(rowNum - 1, rowNum + 2):
            for j in range(colNum - 1, colNum + 2):
                try:
                    if grid[i][j] == -1:
                        self.searchDomain(i, j)[grid[rowNum][colNum]] = -1
                        tmp = [[i, j], [grid[rowNum][colNum]]]
                        removedDomain.append(tmp)
                except Exception as e:
                    pass

    def forwardCheck(self, grid, rowNum, colNum):
        self.NoConChecks += 1
        tmp = []

        for i in range(len(grid[0])):
            if grid[rowNum][i] == -1:
                self.searchDomain(rowNum, i)[grid[rowNum][colNum]] = -1
                tmp1 = [[rowNum, i], [grid[rowNum][colNum]]]
                tmp.append(tmp1)

        SumOfColumn = sum(grid[i][colNum] for i in range(len(grid) - 1) if grid[i][colNum] != -1)
        count = sum(1 for k in range(len(grid) - 1) if grid[k][colNum] == -1)

        for i in range(len(grid) - 1):
            if grid[i][colNum] == -1:
                tmp2 = [[i, colNum], [-1] * 10]

                for s in range(10):
                    tmp2[1][s] = -1

                tmp1 = self.searchDomain(i, colNum)
                for k in range(len(tmp1)):
                    if tmp1[k] != -1:
                        if count >= 2:
                            if tmp1[k] + SumOfColumn > grid[len(grid) - 1][colNum]:
                                tmp2[1][tmp1[k]] = tmp1[k]
                                tmp1[k] = -1
                        else:
                            if tmp1[k] + SumOfColumn != grid[len(grid) - 1][colNum]:
                                tmp2[1][tmp1[k]] = tmp1[k]
                                tmp1[k] = -1
                tmp.append(tmp2)

        self.AdjecentReduction(grid, rowNum, colNum, tmp)
        return tmp
