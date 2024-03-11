
def bin_search(a, x):
    l = -1
    r = len(a)
    while r - l > 1:
        m = (r + l) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    if r == len(a) or a[r] != x:
        return -1
    else:
        return r


def test_bin_search():
    variants = [('1 2 3 4', 3), ('1 2 3 4', 1), ('1 2 3 4', 4),
                ('1 2 3 4', 0), ('1 2 3 4', 5), ('1 2 2 4', 3),
                ('1 2 2 3 4', 2), ('2 2 2 2', 2), ('2', 2),
                ('1 2 2 3 4 7 8', 2), ('1 2 3 4 5 6 6 7 8', 6), ('1 2 3 4 6 6 6 7 8', 6)]
    out_expected = '2 0 3 -1 -1 -1 1 0 0 1 5 4 '

    out = ''
    for line, x in variants:
        a = list(map(int, line.split()))
        out += str(bin_search(a, x)) + ' '

    if out_expected == out:
        print("Good")
    else:
        print("ERROR")
        print(out_expected)
        print(out)


if __name__ == '__main__':
    test_bin_search()

