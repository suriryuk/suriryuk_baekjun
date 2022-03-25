number = int(input())
hansu = 0
before_gap = 0
after_gap = 0


for i in range(1, number + 1):
    numbers = list(map(int, str(i)))
    length = len(numbers)
    if length == 1 or length == 2:
        hansu += 1
    else:
        before_gap = numbers[1] - numbers[0]
        after_gap = numbers[2] - numbers[1]
        if before_gap == after_gap:
            hansu += 1
             
print(hansu)
