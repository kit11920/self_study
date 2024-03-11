
def check(x1, kaz1, y1, x, kaz, y, p, count):
    if y1 <= 0 and kaz1 <= 0:
        return count + 1
    if (kaz1 == kaz and x1 == x and y1 == y) or x <= 0:
        return -1

    if kaz1 <= 0:
        return y_min(x1, kaz1, y1, p, count + 1)
    else:
        c1 = kaz_min(x1, kaz1, y1, p, count + 1)
        c2 = y_min(x1, kaz1, y1, p, count + 1)
        if c2 != -1 and c1 != -1: return min(c1, c2)
        elif c1 != -1: return c1
        elif c2 != -1: return c2
        else: return -1


def kaz_min(x, kaz, y, p, count):
    if kaz <= x:
        kaz1 = 0
        y1 = y - (x - kaz)
        x1 = x - y1
    else:
        kaz1 = kaz - x
        x1 = x - y
        y1 = y + p

    # print(' ' * count, f'{count}:', x, kaz, y)

    return check(x1, kaz1, y1, x, kaz, y, p, count)
    # if y1 <= 0 and kaz1 <= 0:
    #     return count + 1
    # if (kaz1 == kaz and x1 == x and y1 == y) or x <= 0:
    #     return -1
    #
    # if kaz1 <= 0:
    #     return y_min(x1, kaz1, y1, p, count + 1)
    # else:
    #     c1 = kaz_min(x1, kaz1, y1, p, count + 1)
    #     c2 = y_min(x1, kaz1, y1, p, count + 1)
    #     if c2 != -1 and c1 != -1: return min(c1, c2)
    #     elif c1 != -1: return c1
    #     elif c2 != -1: return c2
    #     else: return -1


def y_min(x, kaz, y, p, count):
    if y <= x:
        y1 = 0
        kaz1 = kaz - (x - y)
        x1 = x
    else:
        y1 = y - x
        kaz1 = kaz
        x1 = x - y1
    if kaz1 > 0:
        y1 += p

    # print(' ' * count, f'{count}:', x, kaz, y)

    return check(x1, kaz1, y1, x, kaz, y, p, count)
    # if y1 <= 0 and kaz1 <= 0:
    #     return count + 1
    # if (kaz1 == kaz and x1 == x and y1 == y) or x <= 0:
    #     return -1
    #
    # if kaz1 <= 0:
    #     return y_min(x1, kaz1, y1, p, count + 1)
    #
    # c1 = kaz_min(x1, kaz1, y1, p, count + 1)
    # c2 = y_min(x1, kaz1, y1, p, count + 1)
    # if c2 != -1 and c1 != -1:
    #     return min(c1, c2)
    # elif c1 != -1:
    #     return c1
    # elif c2 != -1:
    #     return c2
    # else:
    #     return -1


def main():
    x = int(input())
    kaz = int(input())
    p = int(input())

    print(kaz_min(x, kaz, 0, p, 0))

main()

# def act(x, kaz, y, p, count):
#     if kaz > x:
#         if x > y:
#             kaz1 = kaz - (x - y)
#             y1 = p
#         else:
#             kaz1 = kaz
#             y1 = y - x + p
#         x1 = 2 * x - y
#     else:
#         y1 = y - x + kaz
#         x1 = 2 * x - y - kaz
#         kaz1 = kaz = 0
#
#     if y1 == 0 and kaz == 0:
#         return count + 1
#     elif x <= 0:
#         return -1
#     elif x == x1 and y == y1 and kaz == kaz1:
#         return -1



