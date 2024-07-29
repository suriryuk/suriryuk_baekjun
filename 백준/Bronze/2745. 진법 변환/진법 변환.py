import string

N, B = input().split()

tables = string.digits + string.ascii_uppercase

result = 0
for i in range(len(N)):
    e = tables.index(N[i])
    result += (e * (int(B) ** (len(N) - i - 1)))

print(result)
