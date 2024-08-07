a, b = map(int, input().split())

if a > b:
    for _ in range(a - b + 1):
        print(a, end=" ")
        a -= 1
else:
    for _ in range(b - a + 1):
        print(b, end=" ")
        b -= 1