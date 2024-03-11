

def str_to_kod_num(str):
    str = str.replace('-', '')
    str = str.replace('(', '')
    str = str.replace(')', '')
    if str[:2] == '+7':
       kod = str[2:5]
       num = str[5:]
    elif str[0] == '8':
        kod = str[1:4]
        num = str[4:]
    else:
        kod = '495'
        num = str

    # print(kod, num)
    return kod, num


if __name__ == '__main__':
    kod0, num0 = str_to_kod_num(input())
    kod1, num1 = str_to_kod_num(input())
    print('YES') if kod0 == kod1 and num0 == num1 else print('NO')
    kod2, num2 = str_to_kod_num(input())
    print('YES') if kod0 == kod2 and num0 == num2 else print('NO')
    kod3, num3 = str_to_kod_num(input())
    print('YES') if kod0 == kod3 and num0 == num3 else print('NO')

