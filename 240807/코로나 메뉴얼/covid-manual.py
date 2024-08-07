m1, m2 = input().split()
n1, n2 = input().split()
l1, l2 = input().split()

count = 0

if m1 == 'Y' and int(m2) >= 37:
    count += 1
if n1 == 'Y' and int(n2) >= 37:
    count += 1
if l1 == 'Y' and int(l2) >= 37:
    count += 1

if count >= 2:
    print('E')
else:
    print('N')