def islandPerimeter(grid):
    row=len(grid)
    col=len(grid[0])
    visited=[[0 for c in range(col)] for r in range(row)]
    answer=0

    x,y=findStart(grid)
    
    # bfs
    q=[]
    q.append([x,y])
    visited[x][y]=1
    _x=[0,0,-1,1]
    _y=[-1,1,0,0]

    while q:
        tx,ty=q.pop()
        answer+=4
        for i in range(4):
            nx=tx+_x[i]
            ny=ty+_y[i]

            if 0<=nx<row and 0<=ny<col and grid[nx][ny]:
                answer-=1
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append([nx,ny])
    return answer

# 출발지 찾기
def findStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return [i,j]


# arr=[[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
arr=[[0,1]]
print(islandPerimeter(arr))