import os
import numpy as np
import time
from pprint import pprint


def get_files_in_folder():
    files = []
    for file_name in os.listdir('puzzles'):
        file_path = os.path.join('puzzles', file_name)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files


def is_safe(board, row, col):
    key = board[row][col]
    for i in range(9):
        if i != col and board[row][i] == key:
            return False
        if i != row and board[i][col] == key:
            return False

    r_start = (row // 3) * 3
    r_end = r_start + 3

    c_start = (col // 3) * 3
    c_end = c_start + 3

    for i in range(r_start, r_end):
        for j in range(c_start, c_end):
            if i != row and j != col and board[i][j] == key:
                return False
    return True


def fill_matrix(board, graph, k, keys, r, rows):
    if not rows:
        k += 1
        rows = list(graph[keys[k]].keys())
    for c in graph[keys[k]][rows[r]]:
        if board[rows[r]][c] > 0:
            continue
        board[rows[r]][c] = keys[k]
        if is_safe(board, rows[r], c):
            if r < len(rows) - 1:
                if fill_matrix(board, graph, k, keys, r + 1, rows):
                    return True
                else:
                    board[rows[r]][c] = 0
                    continue
            else:
                if k < len(keys) - 1:
                    if fill_matrix(board, graph, k + 1, keys, 0, list(graph[keys[k + 1]].keys())):
                        return True
                    else:
                        board[rows[r]][c] = 0
                        continue
                return True
        board[rows[r]][c] = 0
    return False


def build_pos_and_rem(board, pos, rem):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j]:
                if board[i][j] not in pos:
                    pos[board[i][j]] = []
                pos[board[i][j]].append([i, j])
                if board[i][j] not in rem:
                    rem[board[i][j]] = 9
                rem[board[i][j]] -= 1

    for i in range(1, 10):
        if i not in pos:
            pos[i] = []
        if i not in rem:
            rem[i] = 9


def build_graph(board, pos, graph):
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
                if board[r][c] == 0:
                    if r not in graph[k]:
                        graph[k][r] = []
                    graph[k][r].append(c)


def main():
    # files = get_files_in_folder()
    files = [os.path.join('puzzles', 'hard_175')]

    total_time = time.time()

    for file in files:
        print(file)
        board = np.loadtxt(file, dtype=int)

        pos = {}
        rem = {}
        graph = {}

        start = time.time()

        build_pos_and_rem(board, pos, rem)
        rem = {k: v for k, v in sorted(rem.items(), key=lambda item: item[1])}
        build_graph(board, pos, graph)
        key_s = list(rem.keys())
        pprint(graph)
        # fill_matrix(board, graph, 0, key_s, 0, list(graph[key_s[0]].keys()))
        finish = round(time.time() - start, 5)
        print(f'Time: {finish}')

    finish_time = time.time() - total_time
    print(finish_time)


if __name__ == "__main__":

    main()
