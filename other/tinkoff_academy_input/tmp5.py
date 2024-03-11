
def print_arr(arr):
    for i in range(len(arr)):
        print(*arr[i], '')

def put_mina(field, y, x):
    field[y][x] = '*'
    near = []
    if 0 <= y - 1 < len(field): near += [[y - 1, x + i] for i in [-1, 0, 1] if 0 <= x + i < len(field[0])]
    if 0 <= y < len(field): near += [[y, x + i] for i in [-1, 1] if 0 <= x + i < len(field[0])]
    if 0 <= y + 1 < len(field): near += [[y + 1, x + i] for i in [-1, 0, 1] if 0 <= x + i < len(field[0])]

    for i, j in near:
        if field[i][j] != '*':
            field[i][j] += 1
    # print_arr(field)

def main():
    row, col = map(int, input().split())
    field = [[0] * col for _ in range(row)]
    w = int(input())
    for i in range(w):
        x, y = map(int, input().split())
        put_mina(field, x - 1, y - 1)
    print_arr(field)

main()