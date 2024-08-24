a, b, c = map(int, input().split())
sat = False

for i in range(1, (b//c) + 1):
    if c * i >= a and c * i <= b:
        sat = True

if sat == True:
    print('YES')
else:
    print('NO')