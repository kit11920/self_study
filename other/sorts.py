from random import randint
from heap import heap_sort


MERGE_SORT=1
HEAP_SORT=2
INSERTION_SORT=3
FAST_SORT=4
K_STATISTICS=5 # дан неотсортированный массив надо найти число которое в отсортированном массиве стоит на k-ом месте

DO=HEAP_SORT


# сортировка слиянием O( nlog(n) )
######
def merge(a, b):
    n = len(a)
    m = len(b)
    c = [0] * (n + m)
    i = j = k = 0
    while i < n or j < m:
        if j == m or (i < n and a[i] < b[j]):
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1

    return c


def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a

    al = a[:n//2]
    ar = a[n//2:]
    al = merge_sort(al)
    ar = merge_sort(ar)

    return merge(al, ar)
######


# сортировка вставками O(n^2)
def insertion_sort(a):
    for i in range(len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


# быстрая сортировка
# рандомизированный алгоритм O( nlog(n) )
def fast_sort(a, l, r):
    # print(l, r - 1)
    if r - l == 1:
        return
    x = a[randint(l, r - 1)]  # рандомный элемент
    m = l   # индекс x в разделенном массиве
    for i in range(l, r):
        if a[i] < x:
            a[i], a[m] = a[m], a[i]
            m += 1
    # if m == l:
    #     return
    mx = m
    for i in range(m, r):
        if a[i] == x:
            a[i], a[mx] = a[mx], a[i]
            mx += 1

    # print("r", l, m, a[l:m])
    if l != m:
        fast_sort(a, l, m)

    # print("l", mx, r, a[mx:r])
    if mx != r:
        fast_sort(a, mx, r)


def test_sorts(sorting=INSERTION_SORT):
    arrays = ['38 5 7 11 8 27 10 38 14 13 18',
              "3 2 45 -1 0 3 2 2 5 6 34 54 -90 -10 -1",
              '1 1 1 1 1',
              '1 3 5 7 9',
              '89 90 90 3 -1 ']

    for line in arrays:
        a = list(map(int, line.split()))
        print(a)
        if sorting == MERGE_SORT:
            a = merge_sort(a)
        elif sorting == HEAP_SORT:
            heap_sort(a)
        elif sorting == INSERTION_SORT:
            insertion_sort(a)
        elif sorting == FAST_SORT:
            fast_sort(a, 0, len(a))
        print(a)
        print()


# k-я статистика, алгоритм Хоара, O(n)
# дан неотсортированный массив
# надо найти число которое в отсортированном массиве
# стоит на k-ом месте
def k_statistics(a, l, r, k):

    if r - l <= 1:
        return a[k]
    x = a[randint(l, r - 1)]

    m1 = l # l..m1 элементы < x
    for i in range(l, r):
        if a[i] < x:
            a[i], a[m1] = a[m1], a[i]
            m1 += 1

    if k < m1:
        return k_statistics(a, l, m1, k)
    else:
        m2 = m1 # m1..m1 элементы == x
        for i in range(m1, r):
            if a[i] == x:
                a[i], a[m2] = a[m2], a[i]
                m2 += 1

        if k < m2:
            # print(x)
            return x
        else:
            return k_statistics(a, m2, r, k)


def test_k_statistics():
    arrays = ['1 3 5 7 9',
              "3 2 45 -1 0 3 2 2 5 6 34 54 -90 -10 -1",
              '1 1 1 1 1',
              '89 90 90 3 -1 ']

    for line in arrays:
        a = list(map(int, line.split()))
        print(a)

        for i in range(len(a)):
            a_st = a[:]
            a_k = k_statistics(a_st, 0, len(a), i)
            # print(f'a_sorted[{i}] ==', a_k)
            print(a_k, end=' ')
        print()
        fast_sort(a, 0, len(a))
        print(a)
        print()


if __name__ == '__main__':
    if DO == MERGE_SORT:
        test_sorts(MERGE_SORT)
    elif DO == HEAP_SORT:
        test_sorts(HEAP_SORT)
    elif DO == INSERTION_SORT:
        test_sorts(INSERTION_SORT)
    elif DO == FAST_SORT:
        test_sorts(FAST_SORT)
    elif DO == K_STATISTICS:
        test_k_statistics()