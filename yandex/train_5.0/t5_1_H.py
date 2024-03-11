
def main():
    length, x1, v1, x2, v2 = map(int, input().split())

    if x1 == x2:
        print('YES')
        print(0.0)
        return

    vars = list()
    if v1 - v2 != 0:
        t1 = (x2 - x1) / (v1 - v2)
        while t1 < 0 < length / (v1 - v2):
            t1 += length / (v1 - v2)
        if t1 >= 0:
            vars.append(t1)
        else:
            t1 = (x1 - x2) / (v2 - v1)
            while t1 < 0 < length / (v2 - v1):
                t1 += length / (v2 - v1)
            if t1 >= 0:
                vars.append(t1)

        t2 = (length + x2 - x1) / (v1 - v2)
        while t2 < 0 < length / (v1 - v2):
            t2 += length / (v1 - v2)
        if t2 >= 0:
            vars.append(t2)
        else:
            t2 = (length + x1 - x2) / (v2 - v1)
            while t2 < 0 < length / (v2 - v1):
                t2 += length / (v2 - v1)
            if t2 >= 0:
                vars.append(t2)
        # print(f't1, t2 = {t1}, {t2}')
    if v1 + v2 != 0:
        t3 = -(x1 + x2) / (v1 + v2)
        while t3 < 0 < length / (v1 + v2):
            t3 += length / (v1 + v2)
        if t3 >= 0:
            vars.append(t3)

        t4 = (length - x1 - x2) / (v1 + v2)
        while t4 < 0 < length / (v1 + v2):
            t4 += length / (v1 + v2)
        if t4 >= 0:
            vars.append(t4)
        # print(f't3, t4 = {t3}, {t4}')

    if len(vars) == 0:
        print('NO')
    else:
        print('YES')
        print(min(vars))



main()