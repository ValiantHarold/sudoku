import time
import numpy as np


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" "),
        print()


def possible(board, row, col, num):
    for i in range(9):
        if (board[row][i] == num):
            return False

    for i in range(9):
        if (board[i][col] == num):
            return False

    row0 = (row // 3) * 3
    col0 = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if (board[row0 + i][col0 + j] == num):
                return False

    return True


def sudoku_solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if possible(board, row, col, num):
                        board[row][col] = num
                        sudoku_solver(board)
                        board[row][col] = 0
                return


def main():
    board = [[1, 0, 0, 0, 8, 5, 0, 7, 0],
             [0, 0, 0, 0, 0, 2, 0, 0, 9],
             [7, 2, 9, 0, 0, 0, 0, 8, 1],
             [0, 0, 0, 5, 0, 0, 1, 9, 4],
             [9, 0, 0, 6, 2, 0, 0, 5, 3],
             [4, 3, 5, 0, 9, 8, 0, 0, 6],
             [0, 5, 0, 0, 0, 1, 4, 0, 0],
             [2, 0, 7, 0, 0, 4, 5, 0, 0],
             [8, 6, 0, 0, 5, 0, 3, 0, 2]]
    # board = np.array([
    #     [3, 0, 6, 5, 0, 8, 4, 0, 0],
    #     [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #     [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #     [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #     [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #     [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #     [0, 0, 5, 2, 0, 6, 3, 0, 0]
    # ])

    print('Starting board:')
    print_board(board)
    print()

    start = time.time()
    sudoku_solver(board)
    finish = time.time() - start

    print(f'Finished board in {finish}:')
    print_board(board)
    print()


if __name__ == "__main__":

    main()
