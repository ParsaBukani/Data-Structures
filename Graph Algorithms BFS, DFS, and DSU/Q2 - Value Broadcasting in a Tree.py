from collections import deque
import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

tree = [[] for _ in range(1, n+1)]
for i in range(n-1):
    v, u = map(int, input().split())
    if v < u:
        tree[v-1].append(u-1)
    else:
        tree[u-1].append(v-1)

result = [0] * n

def dfs(tree, root, bonus):
    global result
    stack = deque([root])

    while stack:
        node = stack.popleft()
        result[node] += bonus
        for child in tree[node]:
            stack.append(child)
    
for i in range(m):
    a, b = map(int, input().split())
    dfs(tree, a-1, b)

for i in range(n):
    print(result[i], end=' ')
