pseudocode = ''
for _ in range(9):
    row = input()
    pseudocode += row.strip()
pseudocode = eval(pseudocode)

isAppropriate = True
for row in pseudocode:
    numbers = []
    for num in row:
        if num in numbers:
            isAppropriate = False
        elif num != '.':
            numbers.append(num)

if isAppropriate:
    for column in range(9):
        numbers = []
        for r in range(9):
            if pseudocode[r][column] in numbers:
                isAppropriate = False
            elif pseudocode[r][column] != '.':
                numbers.append(pseudocode[r][column])

if isAppropriate:
    i, j = 0, 0
    while i != 9:
        while j != 9:
            numbers = []
            for ro in range(i, i+3):
                for co in range(j, j+3):
                    if pseudocode[ro][co] in numbers:
                        isAppropriate = False
                    elif pseudocode[ro][co] != '.':
                        numbers.append(pseudocode[ro][co])
            j += 3
        i += 3

print("true" if isAppropriate else "false")