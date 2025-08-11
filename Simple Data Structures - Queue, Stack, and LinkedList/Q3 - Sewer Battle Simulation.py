def direction(number):  
    if number > 0:  
        return 1  
    return -1  

queue = eval(input().strip())
mouse1 = 0
mouse2 = 1

while mouse2 < len(queue):
    if direction(queue[mouse1]) != direction(queue[mouse2]) and queue[mouse2] < 0:
        if (abs(queue[mouse1]) < abs(queue[mouse2])):
            queue.pop(mouse1)
            if mouse1 != 0:
                mouse2 -= 1
                mouse1 -= 1
        elif abs(queue[mouse1]) > abs(queue[mouse2]):
            queue.pop(mouse2)
            if mouse2 == len(queue):
                break
        else:
            queue.pop(mouse2)
            queue.pop(mouse1)
            if mouse1 != 0:
                mouse2 -= 1
                mouse1 -= 1
    else:
        mouse1 += 1
        mouse2 += 1


if len(queue) == 0:
    print('[]')
else:
    print('[', end='')
    for i, mouse in enumerate(queue):
        if i == len(queue)-1:
            print(str(mouse) + ']')
        else:
            print(str(mouse) + ",", end='')