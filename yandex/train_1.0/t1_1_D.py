

a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')
elif c == 0:
    if a == 0:
        if b == 0:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        if b % a != 0:
            print('NO SOLUTION')
        else:
            res = - int(b / a)
            print(res)
else:
    if a == 0:
        if b == c ** 2:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        if (c ** 2 - b) % a != 0:
            print('NO SOLUTION')
        else:
            res = int((c ** 2 - b) / a)
            print(res)


