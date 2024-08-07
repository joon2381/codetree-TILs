a, b = input().split()

if a == 'A':
    for i in range(int(b)):
        print(i+1, end=" ")
        i += 1
else:
    for i in range(int(b)):
        print(int(b)-i, end=" ")
        i += 1