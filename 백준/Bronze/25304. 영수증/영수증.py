X = int(input())
N = int(input())

pay = 0
for i in range(N):
    a, b = map(int, input().split())

    pay += (a * b)

print('Yes' if X == pay else 'No')