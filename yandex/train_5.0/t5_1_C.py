

def main():
    out = 0
    n = int(input())
    for i in range(n):
        a = int(input())
        out += a // 4
        a = a % 4
        if a > 1:
            out += 2
        else:
            out += a
    print(out)


main()