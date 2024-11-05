#!/usr/bin/python3
"""
N queens
The N queens puzzle is the challenge of placing N non-attacking
queens on an N*N chessboard.
"""
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    def isSafe(board, row, col):
        for i in range(col):
            if (board[i] == row or
                    board[i] == row - col + i or
                    board[i] == row + col - i):
                return False
        return True

    def solveNQueens(board, col):
        if col == N:
            print(str([[i, board[i]] for i in range(N)]))
            return
        for i in range(N):
            if isSafe(board, i, col):
                board[col] = i
                solveNQueens(board, col + 1)
    solveNQueens([0 for i in range(N)], 0)
