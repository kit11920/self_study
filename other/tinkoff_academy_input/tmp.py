str = input()
if len(str) >= 8:
    little = big = digit = False
    for a in str:
        if a.isalpha() and a.islower():
            little = True
        elif a.isalpha() and a.isupper():
            big = True
        elif a.isdigit():
            digit = True
    if little and big and digit:
        print('YES')
    else:
        print('NO')
else:
    print('NO')