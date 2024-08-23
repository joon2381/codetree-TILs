n = int(input())
add = 1
i = 1
for i in range(1, 11):
    add *= i
    if add >= n:
        break
print(i)