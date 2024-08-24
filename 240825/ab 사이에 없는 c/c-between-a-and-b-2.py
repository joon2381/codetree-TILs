a, b, c = map(int, input().split())

guess = True

for i in range(1, b//c):
    if a >= c * i and b <= c * i:
        guess = False
        break

if guess == True:
    print('YES')
else:
    print('NO')