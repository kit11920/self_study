

def main():
    n, k, d = map(int, input().split())

    rest = 1
    while rest < 10 and d > 0 and rest != 0:
        n *= 10
        rest = k - n % k
        if rest == k:
            d -= 1
            rest = 0
        elif rest < 10:
            n += rest
            d -= 1
        # print(n)
    if rest == 0:
        n = str(n) + '0' * d
        print(n)
    elif rest >= 10:
        print(-1)
    else:
        print(n)





main()