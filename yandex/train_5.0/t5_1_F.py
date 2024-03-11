
def main():
    out = ''
    n = int(input())
    nums = list(map(int, input().split()))
    last = nums[0] % 2
    for i in range(1, n):
        now = nums[i] % 2
        if last and now:
            out += chr(120)
        else:
            out += chr(43)
        last = last or now
        # print(last)

    print(out)


main()