a, b = map(int, input().split())
c = 1
for _ in range(b):
    c *= a
print(c)