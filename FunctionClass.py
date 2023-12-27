import random
import time

class FunctionClass:
    
    @staticmethod
    def checkConstraint(grid, rowNo, colNo, sum_val):
        if FunctionClass.checkRow(grid, rowNo) and FunctionClass.checkSumCoulmn(grid, colNo, sum_val) and FunctionClass.CheckAdjecent(grid, rowNo, colNo):
            return True
        else:
            return False

    @staticmethod
    def checkRow(grid, rowNo):
        SimpleBacktracking.NoConChecks += 1
        ForwardChecking.NoConChecks += 1
        BacktrackingWithMRVHeuristic.NoConChecks += 1
        comp = [-1] * len(grid[0])

        for j in range(len(grid[0])):
            if grid[rowNo][j] >= 0 and comp[grid[rowNo][j]] == -1:
                comp[grid[rowNo][j]] = grid[rowNo][j]
            elif grid[rowNo][j] >= 0 and comp[grid[rowNo][j]] != -1:
                return False
        return True

    @staticmethod
    def checkSumCoulmn(grid, colNo, sum_val):
        SimpleBacktracking.NoConChecks += 1
        ForwardChecking.NoConChecks += 1
        BacktrackingWithMRVHeuristic.NoConChecks += 1

        SumCol = 0
        bool_val = False
        for j in range(len(grid) - 1):
            if grid[j][colNo] != -1:
                SumCol += grid[j][colNo]
            else:
                bool_val = True
        if not bool_val:
            return SumCol == sum_val
        return SumCol <= sum_val

    @staticmethod
    def CheckAdjecent(assignments, rowNum, colNum):
        SimpleBacktracking.NoConChecks += 1
        ForwardChecking.NoConChecks += 1
        BacktrackingWithMRVHeuristic.NoConChecks += 1

        for i in range(rowNum - 1, rowNum + 2):
            for j in range(colNum - 1, colNum + 2):
                if j != colNum and i != rowNum:
                    try:
                        if assignments[rowNum][colNum] == assignments[i][j]:
                            return False
                    except Exception as e:
                        pass
        return True

    @staticmethod
    def generateTennerGrid(grid):
        c = 0
        while not FunctionClass.fillMatrix(grid) and c < 100000:
            FunctionClass.fillMatrix(grid)
            c += 1

        if c >= 100000:
            tmp = [
                [-1, 6, 2, 0, -1, -1, -1, 8, 5, 7],
                [-1, 0, 1, 7, 8, -1, -1, -1, 9, -1],
                [-1, 4, -1, -1, 2, -1, 3, 7, -1, 8],
                [13, 10, 8, 7, 19, 16, 11, 19, 15, 17]
            ]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    grid[i][j] = tmp[i][j]
        else:
            for j in range(len(grid[0])):
                k = sum(grid[i][j] for i in range(len(grid) - 1))
                grid[len(grid) - 1][j] = k

        rand = random.Random()
        limit = 0
        if len(grid) == 4:
            limit = 14
        else:
            limit = 19
        counter = 0
        for i in range(len(grid) - 1):
            for j in range(len(grid[0])):
                if counter >= limit:
                    return
                x = rand.randint(0, i)
                y = rand.randint(0, j)
                if grid[x][y] != -1:
                    grid[x][y] = -1
                    counter += 1

    @staticmethod
    def copy(temp, temp1):
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                temp1[i][j] = temp[i][j]

    @staticmethod
    def fillMatrix(matrix):
        counter = 0
        rand = random.Random()
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i])):
                matrix[i][j] = -1

        while not FunctionClass.isMatrixFilled(matrix):
            for i in range(len(matrix) - 1):
                used = [False] * 10
                rowUsed = [False] * 10
                for j in range(len(matrix[i])):
                    if matrix[i][j] == -1:
                        num = rand.randint(0, 9)
                        counter += 1
                        if counter > 100:
                            return False
                        while used[num] or FunctionClass.isAdjecent(matrix, i, j, num) or rowUsed[num]:
                            num = rand.randint(0, 9)
                        matrix[i][j] = num
                        used[num] = True
                        rowUsed[matrix[i][j]] = True
                    else:
                        rowUsed[matrix[i][j]] = True
        return True

    @staticmethod
    def isAdjecent(matrix, row, col, num):
        if row > 0 and matrix[row - 1][col] == num:
            return True
        if col > 0 and matrix[row][col - 1] == num:
            return True
        if row > 0 and col > 0 and matrix[row - 1][col - 1] == num:
            return True
        if row > 0 and col < len(matrix[row]) - 1 and matrix[row - 1][col + 1] == num:
            return True
        return False

    @staticmethod
    def isMatrixFilled(matrix):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i])):
                if matrix[i][j] == -1:
                    return False
        return True

    @staticmethod
    def isComplete(assignments):
        for i in range(len(assignments) - 1):
            for j in range(len(assignments[0])):
                if assignments[i][j] == -1:
                    return False
        return True

    @staticmethod
    def printTenner(a, nva, nck, start_time, choice):
        for i in range(len(a)):
            for j in range(len(a[0])):
                print(f"  {a[i][j]}  |", end="")
            print()

        if choice != 0:
            print("the number of variable assignments is:", nva)
            print("the number of consistency checks is:", nck)
            print("The total time is:", time.time() - start_time)

    @staticmethod
    def isInDomain(domain, value):
        return value in domain


class Comparator1:
    @staticmethod
    def getSize(a):
        c = 0
        for i in range(len(a)):
            if a[i] != -1:
                c += 1
        return c

    def compare(self, o1, o2):
        if Comparator1.getSize(o1[1]) < Comparator1.getSize(o2[1]):
            return -1
        elif Comparator1.getSize(o1[1]) > Comparator1.getSize(o2[1]):
            return 1
        else:
            return 0



