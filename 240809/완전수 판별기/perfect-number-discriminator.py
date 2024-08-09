n = int(input())
cnt = 0
for i in range(1, n, 1):
    if n % i == 0:
        cnt += i
if cnt == n:
    print('P')
else:
    print('N')