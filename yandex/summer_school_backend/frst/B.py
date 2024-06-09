DELETE = list('<delete>')
LEN_DEL = len(DELETE)
BSPACE = list('<bspace>')
LEN_BSPACE = len(BSPACE)
LEFT = list('<left>')
LEN_LEFT = len(LEFT)
RIGHT = list('<right>')
LEN_RIGHT = len(RIGHT)


def main():
    with open("input.txt", 'r') as f:
        need_str = f.readline().rstrip('\n')
        real_str = list(f.readline().rstrip('\n'))
    # need_str = input()
    # real_str = list(input())
    i = 0  # cursor
    inputed = []

    while len(real_str) > 0:
        if real_str[0].isalpha():
            inputed = inputed[:i] + [real_str.pop(0)] + inputed[i:]
            i += 1
        else:
            if real_str[:LEN_DEL] == DELETE:
                del real_str[:LEN_DEL]
                if i < len(inputed):
                    del inputed[i]
            elif real_str[:LEN_BSPACE] == BSPACE:
                del real_str[:LEN_BSPACE]
                if i > 0:
                    del inputed[i - 1]
                    i -= 1
            elif real_str[:LEN_LEFT] == LEFT:
                del real_str[:LEN_LEFT]
                if i > 0:
                    i -= 1
            elif real_str[:LEN_RIGHT] == RIGHT:
                del real_str[:LEN_RIGHT]
                if i < len(inputed):
                    i += 1
            else:
                print('No')
                return

    inputed = ''.join(inputed)
    if need_str == inputed:
        print('Yes')
    else:
        print('No')

    return

main()
