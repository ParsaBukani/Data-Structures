books = eval(input().strip())
k = int(input())

best_scores = []
max_queue = []

for i in range(len(books)):
    if max_queue and max_queue[0] < i - k + 1:
        max_queue.pop(0)
    
    while max_queue and books[max_queue[-1]] <= books[i]:
        max_queue.pop()
    
    max_queue.append(i)
    
    if i >= k - 1:
        best_scores.append(books[max_queue[0]])

print('[', end='')
for i, book in enumerate(best_scores):
    if i == len(best_scores)-1:
        print(str(book) + ']')
    else:
        print(str(book) + ",", end='')