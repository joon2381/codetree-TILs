n = int(input())


cnt = 0
for i in range(2, n):
    if n % 2 == 0:
        cnt += 1
if cnt == 0:
    print('P')
else:
    print('C')