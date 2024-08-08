a, b = map(int, input().split())

sum1 = 0

for i in range(a, b+1, 1):
    sum1 += i
print(sum1)