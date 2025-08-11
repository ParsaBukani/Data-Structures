import queue

n, m = map(int, input().split())
q = queue.Queue()
q.put((n, 0))

ans  = 0
visited = set()

while not q.empty():
    node = q.get()
    if node[0] == m:
        ans = node[1]
        break
    
    child_1 = (node[0] - 1, node[1] + 1)
    child_2 = (node[0] * 2, node[1] + 1)

    if child_1[0] > 0 and child_1[0] not in visited:
        q.put(child_1)
        visited.add(child_1[0])
    if node[0] < m and child_2[0] not in visited:
        q.put(child_2)
        visited.add(child_2[0])
    
print(ans)
