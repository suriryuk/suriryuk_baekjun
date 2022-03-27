a, b = map(int, input().split())

rev_a = (a % 10) * 100
rev_a += ((a % 100) // 10) * 10
rev_a += (a // 100)

rev_b = (b % 10) * 100
rev_b += ((b % 100) // 10) * 10
rev_b += (b // 100)

if rev_a > rev_b:
    print(rev_a)
elif rev_a < rev_b:
    print(rev_b)