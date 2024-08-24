a, b = map(int, input().split())

guess = False

for i in range(2, 961):
    if 1920 % i == 0 and 2880 % i == 0:
        if a <= i and b >= i:
            guess = True
            break

if guess == True:
    print(1)
else:
    print(0)