# B. Футбольный комментатор

def win(g1, g2, h1, h2, p):
    if g1 + h1 > g2 + h2 or \
            (g1 + h1 == g2 + h2 and
             ((p == 1 and h1 > g2) or (p == 2 and g1 > h2))):
        return True
    return False


def main():
    g1, g2 = map(int, input().split(':'))
    h1, h2 = map(int, input().split(':'))
    p = int(input())

    if win(g1, g2, h1, h2, p):
        x = 0
    else:
        x = (g2 + h2) - (g1 + h1)
        while not win(g1, g2, h1 + x, h2, p):
            x += 1

    print(x)


main()
# if g1 + h1 > g2 + h2 or \
#         (g1 + h1 == g2 + h2 and
#          ((p == 1 and h1 > g1) or (p == 2 and g1 > h2))):
#     x = 0
# else:
#     x = (g2 + h2) - (g1 + h1)
#     if (p == 1 and h1 + x > g1) or (p == 2 and g1 > h1 + x):
#         pass
#     else:
#         x += 1
#
# print(x)