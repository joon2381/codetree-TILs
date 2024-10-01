a = int(input())

for i in range(a):
    if (i+1) % 3 == 0:
        print(0, end=" ")
    else:
        print(i+1, end=" ")