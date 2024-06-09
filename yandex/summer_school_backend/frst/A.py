def main():
    digit = False
    big_alpha = False
    little_alpha = False
    res = 'NO'

    name = input()
    if len(name) >= 8:
        for a in name:
            if a.isdigit():
                digit = True
            elif a.isalpha():
                if a.islower():
                    little_alpha = True
                else:
                    big_alpha = True
        if digit and little_alpha and big_alpha:
            res = 'YES'

    print(res)

main()
