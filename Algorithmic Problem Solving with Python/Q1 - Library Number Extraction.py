card = input()
card = card[1:-1]
card = card.strip()
number = ""
for ch in card:
    if ((ch == '-' or ch == '+') and len(number) == 0) or ch.isdigit():
        number += ch
    else:
        break

contains_number = any(char.isdigit() for char in number)
if contains_number:
    number = int(number)
else:
    number = 0
if number > (2**31 - 1):
    number = 2**31 -1
elif number < (-2**31):
    number = -2**31

print(number)