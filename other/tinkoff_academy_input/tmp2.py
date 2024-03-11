n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            count += 1
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(count)
# for i in range(n):
#     min_el = min(arr)
#     ind = arr.index(min_el)
#     count += ind
#     # print(f"{arr}, min_ind - {ind}")
#     arr = arr[:ind] + arr[ind + 1:]
#     # print(arr)


# print(count)
# print(arr)




#