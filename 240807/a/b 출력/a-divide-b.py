a, b = map(int, input().split())
cnt = 0
for _ in range(21):
    c = a//b
    print(c, end="")
    if cnt == 0 and c//10 == 0:
        print('.', end="")
        cnt += 1
    if a < b:
        a = a*10 - b*c
    else:
        a = a - (b * c)
        a *= 10