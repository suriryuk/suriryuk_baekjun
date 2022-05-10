num = []
N = int(input())

for i in range(N):
    a = int(input())
    num.append(a)
    
for i in range(len(num)):
    for j in range(i, len(num)):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]

for i in range(len(num)):
    print(num[i])