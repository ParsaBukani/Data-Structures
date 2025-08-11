import sys  
from collections import defaultdict  

input = sys.stdin.read  

data = list(map(int, input().split()))  
n = data[0]  
index = 1  

cordinates = []

for _ in range(n):  
    p1 = data[index]  
    p2 = data[index + 1]  

    cordinates.append((p1, 1))
    cordinates.append((p2 + 1, -1)) 

    index += 2  

cordinates.sort()  

sum = 0  
counts = [0] * n  
current_position = None  

for position, event_type in cordinates:  
    if current_position is not None and position != current_position:  
        counts[sum - 1] += (position - current_position)    

    current_position = position  
    sum += event_type  

print(" ".join(map(str, counts)))