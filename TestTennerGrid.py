import time

def main():
    no_of_rows = 4

    grid = [[0] * 10 for _ in range(no_of_rows)]

    generate_tenner_grid(grid)
    print("The initial state is:")
    print("========================")
    print_tenner(grid, 0, 0, 0, 0)
    print()

    while True:
        print("1- Simple backtracking")
        print("2- Backtracking with forward checking")
        print("3- Backtracking with MRV")
        print("4- Exit")
        choice = int(input("Enter a choice: "))

        if choice == 1:
            grid1 = [row[:] for row in grid]
            simple_backtracking = SimpleBacktracking()
            simple_backtracking.simple_backtracking_search(grid1)
        elif choice == 2:
            grid2 = [row[:] for row in grid]
            forward_checking = ForwardChecking()
            forward_checking.forward_checking_search(grid2)
        elif choice == 3:
            grid3 = [row[:] for row in grid]
            backtracking_mrv = BacktrackingWithMRVHeuristic()
            backtracking_mrv.backtracking_mrv_search(grid3)
        elif choice == 4:
            print("Bye")
            break
        else:
            print("Choice not valid")


def generate_tenner_grid(grid):
    # Implement the logic for generating a Tenner grid
    pass


def print_tenner(grid, var_assigned, con_checks, start_time, arg):
    # Implement the logic for printing the Tenner grid
    pass


def is_complete(grid):
    # Implement the logic for checking if the grid is complete
    pass


def check_constraint(grid, i, j, value):
    # Implement the logic for checking constraints
    pass


class SimpleBacktracking:
    def __init__(self):
        self.NoVarAssigned = 0
        self.NoConChecks = 0
        self.start_time = 0

    def simple_backtracking_search(self, grid):
        self.NoVarAssigned = 0
        self.NoConChecks = 0
        self.start_time = time.time()

        # Implement the logic for simple backtracking search
        pass


class ForwardChecking:
    def __init__(self):
        self.NoVarAssigned = 0
        self.NoConChecks = 0
        self.start_time = 0

    def forward_checking_search(self, grid):
        self.NoVarAssigned = 0
        self.NoConChecks = 0
        self.start_time = time.time()

        # Implement the logic for forward checking search
        pass


class BacktrackingWithMRVHeuristic:
    def __init__(self):
        self.NoVarAssigned = 0
        self.NoConChecks = 0
        self.start_time = 0

    def backtracking_mrv_search(self, grid):
        self.NoVarAssigned = 0
        self.NoConChecks = 0
        self.start_time = time.time()

        # Implement the logic for backtracking with MRV search
        pass


if __name__ == "__main__":
    main()
