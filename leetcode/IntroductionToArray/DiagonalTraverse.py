matrix=[]

result=[]
if len(matrix):
    return result
    
row=len(matrix)-1
col=len(matrix[0])-1

i,j=0,0
add=0
while 1:
    result.append(matrix[i][j])

    if i==row and j==col:
        break

    # 홀수 올라감 add=0
    if (i==0 or j == col) and add==0:
        if j==col:
            i+=1
        else:
            j+=1
        add=1
    elif (j==0 or i==row) and add==1:
        if i==row:
            j+=1
        else:
            i+=1
        add=0
    elif add==1:
        i+=1
        j-=1
    else:
        i-=1
        j+=1


print(result)    

