n = int(input())

odd_sum = 0

for _ in range(n):
    i = int(input())

    if i % 2 == 1 and i % 3 == 0:
        odd_sum += i
print(odd_sum)