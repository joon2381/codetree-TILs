a = int(input())
num = 0
i = 0
for i in range(100):
    num += i
    if num >= a:
        break
print(i)