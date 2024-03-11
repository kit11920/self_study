# GOOOOOOD!
SECH = 1.618
EPS = 0.01


def count_steps(a, c):
    count = 0
    while a > 0 and c > 0:
        c1 = c - a
        a1 = 2 * a - c
        if a1 == a and c1 == c:
            return -1
        a, c = a1, c1
        count += 1
    if a > 0:
        return count
    else:
        return -1


def attack_c(a, b, c, p):
    if c > a:
        c1 = c - a
        b1 = b
    else:
        c1 = 0
        b1 = b - (a - c)
    a1 = max(a - c1, 0)
    if b1 > 0:
        c1 += p
    return a1, b1, c1


def main():
    a = int(input())
    b = int(input())
    c = 0
    p = int(input())
    count = 0

    while b > a > 0:
        a1, b1, c1 = attack_c(a, b, c, p)
        if a1 == a and b1 == b and c1 == c:
            print(-1)
            return
        else:
            a, b, c = a1, b1, c1
        count += 1

    vars = list()
    while 0 <= b <= a:
        # пробуем добить казарму
        c1 = max(c - (a - b), 0)
        a1 = max(2 * a - c - b, 0)
        if 1: # (c1 > a1 and abs(c1 / a1 - SECH) <= EPS) or (a1 > c1 and abs(a1 / c1 - SECH) <= EPS):
            count1 = count_steps(a1, c1)
            if count1 >= 0:
                vars.append(count1 + 1 + count)
        a1, b1, c1 = attack_c(a, b, c, p)
        if a1 == a and b1 == b and c1 == c:
            break
        else:
            a, b, c = a1, b1, c1
        count += 1

    if len(vars) == 0 or a <= 0:
        print(-1)
    else:
        print(min(vars))



main()