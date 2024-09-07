import os
import random
import numpy as np


def determine_difficulty(missing):
    if missing <= 29:
        return "baby"
    elif 30 <= missing <= 45:
        return "easy"
    elif 46 <= missing <= 55:
        return "medium"
    elif 56 <= missing <= 65:
        return "hard"
    elif 66 <= missing:
        return "impossible"


def get_puzzle_count(difficulty):
    file_name = f"{difficulty}_count.txt"
    file_path = os.path.join('count', file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            count = int(file.read())
    else:
        count = 1
    return count


def update_puzzle_count(difficulty, count):
    file_name = f"{difficulty}_count.txt"
    file_path = os.path.join('count', file_name)
    with open(file_path, 'w') as file:
        file.write(str(count + 1))


def is_valid(board, row, col, num):
    return (
        all(num != board[row][i] for i in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[(row // 3) * 3 + i][(col // 3) * 3 + j]
            for i in range(3) for j in range(3))
    )


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = random.sample(range(1, 10), 9)
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def generate_board():
    board = np.zeros((9, 9), dtype=int)
    solve(board)
    return board


def remove_values(board, missing):
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)

    for i, j in positions[:missing]:
        board[i][j] = 0


def main():
    for _ in range(100):

        missing = random.randint(30, 73)
        board = generate_board()

        missing_board = board.copy()
        remove_values(missing_board, missing)

        difficulty = determine_difficulty(missing)
        count = get_puzzle_count(difficulty)
        file_name = f'{difficulty}_{str(count).zfill(3)}'

        file_path = os.path.join('puzzles', file_name)
        np.savetxt(file_path, missing_board, fmt="%d", delimiter=" ")

        update_puzzle_count(difficulty, count)


if __name__ == "__main__":
    main()
