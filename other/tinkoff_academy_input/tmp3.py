n = int(input())
lenn = 0
a = list()
for i in range(n):
    beg, end = map(int, input().split())
    if len(a) == 0:
        a = [beg, end]
    else:
        if beg < a[1]:
            a = [a[0], max(a[1], end)]
        else:
            lenn += a[1] - a[0]
            a = [beg, end]
lenn += a[1] - a[0]
print(lenn)