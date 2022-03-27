number = input()
total = 0

for i in number:
    if i in "ABC":
        total += 3
    elif i in "DEF":
        total += 4
    elif i in "GHI":
        total += 5
    elif i in "JKL":
        total += 6
    elif i in "MNO":
        total += 7
    elif i in "PQRS":
        total += 8
    elif i in "TUV":
        total += 9
    elif i in "WXYZ":
        total += 10
        
print(total)