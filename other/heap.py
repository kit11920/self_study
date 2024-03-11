# Куча. Сортировка кучей
# Куча - родитель меньше чем дети
# (i - 1) // 2 - обращение к родителю элемента i
# 2i+1 2i+2 - обращение к детям элемента i


# Добавление в кучу нового элемента с сохранением структуры
def insert(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


# Удаление из кучи минимального элемента
# С просеиванием вниз последнего элемента, который поместили в начало
def remove_min(heap):
    res = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    n = len(heap)
    i = j = 0
    while True:
        if 2*i+1 < n and heap[2*i+1] < heap[j]:
            j = 2*i+1
        if 2*i+2 < n and heap[2*i+2] < heap[j]:
            j = 2*i+2
        if i == j:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i = j
    return res


# затрачивает слишком много места
def heap_sort_bad(a):
    n = len(a)
    heap = list()
    for i in range(n):
        insert(heap, a[i])

    for i in range(n):
        a[i] = remove_min(heap)


def shift_up(heap, i):
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def shift_down(heap, n):    # n = heap_len
    i = j = 0
    while True:
        if 2 * i + 1 < n and heap[2 * i + 1] < heap[j]:
            j = 2 * i + 1
        if 2 * i + 2 < n and heap[2 * i + 2] < heap[j]:
            j = 2 * i + 2
        if i == j:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i = j


def heap_sort(a):
    n = len(a)
    for i in range(n):
        shift_up(a, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        shift_down(a, i)
        # print('    ', a)
    a.reverse()

