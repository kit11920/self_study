
data = list()
for i in range(3):
    data.append(int(input()))

if (sum(data) - max(data) > max(data)):
    print('YES')
else:
    print('NO')