numRows=5

result=[[1]]
if numRows == 0:
    print()
if numRows == 1:
    print(result)

for i in range(0,numRows-1):
    result.append([1])
    for j in range(len(result[i])-1):
        result[i+1].append(result[i][j]+result[i][j+1])
    result[i+1].append(1)

print(result)