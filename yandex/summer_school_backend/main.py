
def add_sorted(arr, elem, ind):
    i = len(arr)
    arr.append((elem, ind))
    while i - 1 >= 0 and arr[i - 1][0] > arr[i][0]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
        i -= 1


def main():
    summa = 0
    days_buys = []

    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    if K == 1:
        print(sum(c))
        print(*[1] * N)
        return
    j = 0
    minimums = [(c[0], 0)]
    # min_cost = c[0]
    summa += minimums[0][0]
    days_buys.append(1)
    for i in range(1, N):
        if c[i] < minimums[0][0]:
            days_buys += [0] * (i - (len(days_buys) - 1))
            days_buys[-1] += 1
            summa += c[i]
        else:
            days_buys[-1] += 1
            summa += minimums[0][0]

        add_sorted(minimums, c[i], i)
        if i + 1 - j == K:
            if c[j] == minimums[0][0]:

                # ind = c[j + 1:].index(minimums[1]) + j + 1
                ind = minimums[1][1]
                days_buys += [0] * (ind - (len(days_buys) - 1))
                del minimums[0]
            else:
                ind = 0
                for qq in range(len(minimums)):
                    if minimums[qq][0] == c[j]:
                        del minimums[qq]
                        break
                # del minimums[minimums.index(c[j])]

            j += 1


    days_buys += [0] * (N - len(days_buys))
    print(summa)
    print(*days_buys)





main()
