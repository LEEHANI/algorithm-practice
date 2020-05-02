# matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# matrix=[
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12]
# ]


for m in matrix:
    print(m)

result=[]
        
if len(matrix) == 0:
    # return []
    pass

row=len(matrix)-1
col=len(matrix[0])-1
size=(row+1)*(col+1)
i,j=0,0
move,d=0,0
direction=[[0,1],[1,0],[0,-1],[-1,0]]

while 1:

    result.append(matrix[i][j])

    if size==len(result):
        break

    # 오른쪽 위 
    if i==0+move and j==col-move and d==0:
        d+=1
    # 오른쪽 아래 
    elif i==row-move and j==col-move and d==1:
        d+=1
    # 왼쪽 아래 
    elif i==row-move and j==0+move and d==2:
        d+=1
    # 왼쪽 위 
    elif i==1+move and j==0+move and d==3:
        d+=1
        move+=1

    i+=direction[d%4][0]
    j+=direction[d%4][1]
    d=d%4

print(result)


