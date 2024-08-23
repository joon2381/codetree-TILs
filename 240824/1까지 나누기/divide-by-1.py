n = int(input())

i = 1
for i in range(1, 101):
    n //= i
    if n <= 1:
        break
print(i)