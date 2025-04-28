dial_chars = {
    1 : '',
    2 : 'ABC',
    3 : 'DEF',
    4 : 'GHI',
    5 : 'JKL',
    6 : 'MNO',
    7 : 'PQRS',
    8 : 'TUV',
    9 : 'WXYZ'
}

dial = input()

time = 0
for ch in dial:
    for key, value in dial_chars.items():
        if ch in value:
            time += (key + 1)
print(time)