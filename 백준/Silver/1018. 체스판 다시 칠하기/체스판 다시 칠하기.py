import sys

N, M = sys.stdin.readline().rstrip().split(" ")


def change_color(value):
    if value == "B":
        return "W"
    else:
        return "B"


def counting(board, r_index, c_index):
    color = board[r_index][c_index]
    draw_count = 0
    for i in range(r_index, r_index + 8):
        for j in range(c_index, c_index + 8):

            if j == c_index:
                if board[i][j] != color:
                    draw_count += 1
                    color = change_color(board[i][j])
                else:
                    color = board[i][j]
            else:
                if board[i][j] == color:
                    draw_count += 1
                    color = change_color(board[i][j])
                else:
                    color = board[i][j]

    return min(draw_count, 64 - draw_count)


board = []
for _ in range(int(N)):
    tmp = sys.stdin.readline().rstrip()
    board.append(tmp)

min_value = 50 * 50
for s_index_r in range(int(N) - 8 + 1):
    for s_index_c in range(int(M) - 8 + 1):
        tmp_mean_value = counting(board, s_index_r, s_index_c)
        if min_value >= tmp_mean_value:
            min_value = tmp_mean_value
print(min_value)
