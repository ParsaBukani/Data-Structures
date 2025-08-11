matrix = eval(input().strip())

path = []
while True:
    for col in range(len(matrix[0])):
        path.append(matrix[0][col])

    matrix.pop(0)
    if len(matrix) == 0:
        break
    
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) -1 , -1, -1)]
    matrix = transposed_matrix

print(path)