import sys  
from collections import defaultdict  


class DisjointUnionSets:  
    def __init__(self, n):  
        self.rank = [0] * n  
        self.parent = list(range(n))  

    def find(self, x):  
        if self.parent[x] != x:  
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]  

    def unionSets(self, x, y):  
        xRoot = self.find(x)  
        yRoot = self.find(y)  
        if xRoot == yRoot:  
            return  
        if self.rank[xRoot] < self.rank[yRoot]:  
            self.parent[xRoot] = yRoot  
        elif self.rank[yRoot] < self.rank[xRoot]:  
            self.parent[yRoot] = xRoot  
        else:  
            self.parent[yRoot] = xRoot  
            self.rank[xRoot] += 1  


input = sys.stdin.read  
data = input().split()  

N = int(data[0])  
M = int(data[1])  

permutation = list(map(int, data[2:N+2]))  

dsu = DisjointUnionSets(N)  

index = N + 2  
for _ in range(M):  
    a = int(data[index]) - 1  
    b = int(data[index + 1]) - 1  
    dsu.unionSets(a, b)  
    index += 2  

components = defaultdict(list)  
for i in range(N):  
    root = dsu.find(i)  
    components[root].append(i)  

max_cleanliness = 0  

for indices in components.values():  
    index_set = set(indices)
    correct_positions = sum(1 for i in indices if permutation[i] - 1 in index_set)  
    max_cleanliness += correct_positions  

print(max_cleanliness)