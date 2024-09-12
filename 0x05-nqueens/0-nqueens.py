#!/usr/bin/python3
"""
N Queens Solver
This module solves the N Queens problem using backtracking.
"""
import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """Solve the N Queens problem and return all solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        """Recursive function to solve N Queens problem"""
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True

        res = False
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                res = solve(col + 1) or res
                board[i][col] = 0
        return res

    solve(0)
    return solutions


def print_solutions(solutions):
    """Print the solutions in the required format"""
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)
