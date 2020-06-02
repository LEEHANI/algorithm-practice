grid=[]


def bfs(sx,sy,col,row,grid,visited):
    _x=[0,0,-1,1]
    _y=[-1,1,0,0]

    q=[[sx,sy]]
    visited[sx][sy]=1

    while q:
        x,y=q.pop(0)
        for i in range(4):
            nx=x+_x[i]
            ny=y+_y[i]
            if 0<=nx<row and 0<=ny<col and grid[nx][ny]=='1' and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=1 

row=len(grid)
answer=0
if row:
    col=len(grid[0])
    visited=[[0 for col in range(col)] for row in range(row)]

    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1' and visited[i][j]==0:
                bfs(i,j,col,row,grid,visited)
                answer+=1

print(answer)