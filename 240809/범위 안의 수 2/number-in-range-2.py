asd = 0
cnt = 0
for _ in range(10):
    n = int(input())

    if n >= 0 and n <= 200:
        cnt += 1
        asd += n
print(asd, '%.1f' % (asd/cnt))