t = int(input())


for _ in range(t):
    summ = 0
    l, r = map(int, input().split())
    for a in range(l, r + 1):
        if a == 0:
            summ += -1 * (r - l + 1)
        elif a == 1:
            pass
        else:
            sr = int(a * (a ** r - 1) / (a - 1))
            sl_ = int(a * (a ** (l - 1) - 1) / (a - 1))
            summ += (a - 1) * (sr - sl_)
    print(summ)