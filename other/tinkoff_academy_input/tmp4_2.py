t = int(input())
for _ in range(t):
    summ = 0
    l, r = map(int, input().split())
    for a in range(l, r + 1):
        for b in range(l, r + 1):
            summ += a ** b * (a - 1)
    print(summ)