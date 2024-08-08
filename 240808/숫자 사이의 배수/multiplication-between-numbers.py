a, b = map(int, input().split())

sum1 = 0
cnt = 0
for i in range(a, b+1, 1):
    if i % 5 == 0 or i % 7 == 0:
        sum1 += i
        cnt += 1
print(sum1, "%.1f" % (sum1 / cnt))