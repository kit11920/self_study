SEEN = '-'


def print_arr(arr):
    for i in range(len(arr)):
        print(' '.join(arr[i]))
    print('\n')


def not_figure(char):
    return char == SEEN or char == '*'


def see_R(board, x, y):
    i = x - 1
    while i >= 0 and not_figure(board[i][y]):
        board[i][y] = SEEN
        i -= 1
    i = x + 1
    while i < 8 and not_figure(board[i][y]):
        board[i][y] = SEEN
        i += 1
    i = y - 1
    while i >= 0 and not_figure(board[x][i]):
        board[x][i] = SEEN
        i -= 1
    i = y + 1
    while i < 8 and not_figure(board[x][i]):
        board[x][i] = SEEN
        i += 1

def see_B(board, x, y):
    for p in [1, -1]:
        for q in [1, -1]:
            i, j = x + p, y + q
            while 0 <= i < 8 and 0 <= j < 8 and not_figure(board[i][j]):
                board[i][j] = SEEN
                i, j = i + p, j + q

def main():
    board = list()
    for i in range(8):
        str = list(input()[:8])
        board.append(str)

    cells = 8 * 8
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                see_R(board, i, j)
            elif board[i][j] == 'B':
                see_B(board, i, j)
    # print_arr(board)
    for i in range(8):
        for j in range(8):
            if board[i][j] != '*':
                cells -= 1
    print(cells)



main()