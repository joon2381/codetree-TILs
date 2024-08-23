a = int(input())
num = 0
for i in range(100):
    if num + i > a:
        break
    num += i
print(num)