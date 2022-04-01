a, b, c = map(int, input().split())

if a == b and b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif c == b:
    print(1000 + c * 100)
else:
    if a > b:
        if a > c:
            print(a * 100)
        elif a < c:
            print(c * 100)
    elif b > a:
        if b > c:
            print(b * 100)
        elif b < c:
            print(c * 100)
    elif c > a:
        if c > b:
            print(c * 100)
        elif c < b:
            print(b * 100)