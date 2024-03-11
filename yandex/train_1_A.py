
troom, tcond = map(int, input().split())
act = input()
if ((act == 'freeze' and troom > tcond) or
    (act == 'heat' and troom < tcond) or
    act == 'auto'):
    print(tcond)
else:
    print(troom)




