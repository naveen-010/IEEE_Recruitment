List1 =  [3, 4, 5, 1, 4, 6, 1, 7, 7]
List2 = [5, 8, 2, 9, 9, 4, 6, 3]

AnsList = []

for i in range(len(List1)):
    if List1[i] in List2 and List1[i] not in AnsList:
        AnsList.append(List1[i])

AnsList