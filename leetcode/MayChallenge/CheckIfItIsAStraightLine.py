'''
일직선이되는 조건을 생각해보자 

분수꼴로 나타내서 풀 수 있음 

'''
from math import gcd

# coordinates=[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]] # False
# coordinates=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] # True
# coordinates=[[1,1],[2,2],[3,3],[4,4],[5,5],[7,7]] # True
# coordinates=[[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]] # True
coordinates=[[0,1],[1,3],[-4,-7],[5,11]] # True



disX,disY=abs((coordinates[1][0]-coordinates[0][0])),abs((coordinates[1][1]-coordinates[0][1]))
x,y=coordinates[1]
g=gcd(disX,disY)

if g!= 1:
    disX=disX//g
    disY=disY//g
print(disX, disY)

for i in range(2,len(coordinates)):

    tempX=abs(coordinates[i][0]-x)
    tempY=abs(coordinates[i][1]-y)
    tempG=gcd(tempX, tempY)

    if tempG !=1:
        tempX=tempX//tempG
        tempY=tempY//tempG

    # 1. 일정한 비율로 증가하거나 
    # 2. x or y 값이 고정
    if (disX==tempX and disY == tempY) or (x==coordinates[i][0]) or (y==coordinates[i][1]):
        x,y=coordinates[i]
        continue
    else:
        print(False)
        break
else:
    print(True)

