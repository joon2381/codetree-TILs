a = int(input())

for i in range(a):
    if (i+1) % 3 == 0 or (i+1) % 10 == 3 or (i+1) % 10 == 6 or (i+1) % 10 == 9:
        print(0, end=" ")
    else:
        print(i+1, end=" ")