a, b, c = map(int, input().split())

if a >= b and a >= c:
    print(a)
elif a <= b and b >= c:
    print(b)
else:
    print(c)