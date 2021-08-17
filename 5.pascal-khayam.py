pascal_khayam=[]

n=int (input("Plz enter number row: "))

for i in range(n):
    list=[]
    for j in range(i+1):
        if j == 0 or j==i:
            list.append(1)
        else:
            list.append(pascal_khayam[i-1][j-1]+pascal_khayam[i-1][j])
    pascal_khayam.append(list)

for i in range(len(pascal_khayam)):
    for j in range(len(pascal_khayam[i])):
        print(pascal_khayam[i][j],end=" ")

    print()








