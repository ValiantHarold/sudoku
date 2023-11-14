import os
import numpy as np
import time


def get_files_in_folder():
    files = []
    for file_name in os.listdir('puzzles'):
        file_path = os.path.join('puzzles', file_name)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files


def empty_loc(board, l):
    for row in range(9):
        for col in range(9):
            if (board[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def is_safe(board, row, col, num):
    return (not check_row(board, row, num) and
            (not check_col(board, col, num) and
            (not check_box(board, row - row % 3,
                           col - col % 3, num))))


def check_row(board, row, num):
    for i in range(9):
        if (board[row][i] == num):
            return True
    return False


def check_col(board, col, num):
    for i in range(9):
        if (board[i][col] == num):
            return True
    return False


def check_box(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if (board[i + row][j + col] == num):
                return True
    return False


def sudoku_solver(board):
    l = [0, 0]

    if not empty_loc(board, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):

        if (is_safe(board, row, col, num)):

            board[row][col] = num

            if (sudoku_solver(board)):
                return True

            board[row][col] = 0

    return False


def main():
    files = [os.path.join('puzzles', 'easy_001')]
    # files = get_files_in_folder()

    total_time = time.time()

    for file in files:
        board = np.loadtxt(file, dtype=int)

        start = time.time()
        sudoku_solver(board)
        finish = round(time.time() - start, 4)
        print(f'Time: {finish}')
        print(board)

    finish_time = time.time() - total_time
    print(finish_time)


if __name__ == "__main__":

    main()
