old_sum = 0
cnt = 0

while True:
    old = int(input())

    if old < 20 or old >= 30:
        break
    cnt += 1
    old_sum += old

print('%.2f' % (old_sum/cnt))