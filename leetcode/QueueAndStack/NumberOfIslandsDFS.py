grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]


def dfs(x,y, _x,_y,row,col,visited,grid):
    visited[x][y]=1
    for i in range(4):
        nx=x+_x[i]
        ny=y+_y[i]

        if 0<=nx<row and 0<=ny<col and visited[nx][ny]==0 and grid[nx][ny]=='1':
            dfs(nx,ny,_x,_y,row,col,visited,grid)



row=len(grid)
col=len(grid[0])
visited=[[0 for col in range(col)] for row in range(row)]

_y=[-1,1,0,0]
_x=[0,0,-1,1]
answer=0
for i in range(row):
    for j in range(col):
        if grid[i][j]=='1' and visited[i][j]==0:
            dfs(i,j,_x,_y,row,col,visited,grid)
            answer+=1

print(answer)