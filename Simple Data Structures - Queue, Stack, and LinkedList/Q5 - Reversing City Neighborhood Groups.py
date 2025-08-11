line = input()  
houses, x = line.split(', x = ')  
houses = eval(houses.strip())  
x = int(x.strip())


for group in range(0, len(houses), x):
    if group + x > len(houses):
        break
    
    i, j = (group, group+x-1)
    while i != j and (j-i>0):
        houses[i], houses[j] = houses[j], houses[i]
        i += 1
        j -= 1

print('[', end='')
for i, house in enumerate(houses):
    if i == len(houses)-1:
        print(str(house) + ']')
    else:
        print(str(house) + ",", end='')