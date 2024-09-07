import os
import time
import numpy as np
from util import print_board, get_puzzles


def build_pos_and_rem(board):
    pos = {i: [] for i in range(1, 10)}
    rem = {i: 9 for i in range(1, 10)}

    for i in range(9):
        for j in range(9):
            if board[i][j]:
                pos[board[i][j]].append([i, j])
                rem[board[i][j]] -= 1

    rem = {k: v for k, v in sorted(
        rem.items(), key=lambda item: item[1]) if v != 0}

    return pos, rem


def build_graph(board, pos):
    graph = {}

    for k, v in pos.items():
        if k not in graph:
            graph[k] = {}

        row = list(range(9))
        col = list(range(9))

        for cord in v:
            row.remove(cord[0])
            col.remove(cord[1])

        if len(row) == 0 or len(col) == 0:
            continue

        for r in row:
            for c in col:
                if board[r][c] != 0:
                    continue
                if r not in graph[k]:
                    graph[k][r] = []
                graph[k][r].append(c)

    return graph


def is_safe(board, row, col, key):

    if key in board[row, :]:
        return False

    if key in board[:, col]:
        return False

    r_start, c_start = 3 * (row // 3), 3 * (col // 3)
    r_end, c_end = r_start + 3, c_start + 3

    subboard = board[r_start:r_end, c_start:c_end]

    if key in subboard:
        return False

    return True


def solve(board, graph, keys, k, rows, r):
    for c in graph[keys[k]][rows[r]]:
        if board[rows[r]][c] > 0:
            continue
        if is_safe(board, rows[r], c, keys[k]):
            board[rows[r]][c] = keys[k]
            if r < len(rows) - 1:
                if solve(board, graph, keys, k, rows, r + 1):
                    return True
                else:
                    board[rows[r]][c] = 0
                    continue
            else:
                if k < len(keys) - 1:
                    if solve(board, graph, keys, k + 1, list(graph[keys[k + 1]].keys()), 0):
                        return True
                    else:
                        board[rows[r]][c] = 0
                        continue
                return True
        board[rows[r]][c] = 0
    return False


def main():
    files = get_puzzles()

    total_time = time.time()

    for file in files:
        # print(file[8:])
        board = np.loadtxt(file, dtype=int)
        # start = time.time()
        pos, rem = build_pos_and_rem(board)
        graph = build_graph(board, pos)

        keys = list(rem.keys())
        rows = list(graph[keys[0]].keys())

        solve(board, graph, keys, 0, rows, 0)
        # finish = time.time() - start
        # print(f'Time: {round(finish, 6)}')

    finish_time = time.time() - total_time
    print(finish_time)


if __name__ == "__main__":
    main()
