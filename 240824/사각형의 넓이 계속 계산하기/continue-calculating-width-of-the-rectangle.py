while True:
    w, h, a = map(str, input().split())
    w = int(w)
    h = int(h)

    print(w*h)
    if a == 'C':
        break