result = []
List = []

while (key := input().split()) != ['6']:
    if key[0] == '1':
        List = []

    if key[0] == '2':
        List = None

    if key[0] == '3':
        if List == None:
            result.append("nulle")
        else:
            List.append(key[1])

    if key[0] == '4':
        if List == None:
            result.append("nulle")
        elif int(key[1]) >= len(List):
            result.append("oute")
        else:
            result.append(List[int(key[1])])

    if key[0] == '5':
        if int(key[2]) == 0:
            result.append("sefre")
        else:
            result.append(int(key[1]) // int(key[2]))

for i in range(len(result)):
    print(result[i])