t = int(input())


for _ in range(t):
    summ = 0
    l, r = map(int, input().split())
    for a in range(l, r + 1):
        last_a = a ** l
        # print(last_a)
        part_sum = 0
        for b in range(l + 1, r + 2):
            part_sum += last_a
            last_a *= a
        part_sum *= a - 1
        # print(part_sum)
        summ += part_sum
    print(summ)