a, b, c = map(int, input().split())

result = 0
if a == b:
    if b == c:
        # 모두 같을 때
        result = 10000 + a * 1000
    else:
        # 2개 같은 눈일 때 ( a == b != c )
        result = 1000 + a * 100
elif a == c:
    if a != b:
        # 2개 같은 눈일 때 ( a == c, a != b, b != c )
        result = 1000 + a * 100
elif b == c:
    if a != b:
        # 2개 같은 눈일 때 ( a != b == c )
        result = 1000 + b * 100
else:
    if a > b:
        if a > c:
            result = a * 100
        else:
            result = c * 100
    elif b > c:
        result = b * 100
    else:
        result = c * 100

print(result)