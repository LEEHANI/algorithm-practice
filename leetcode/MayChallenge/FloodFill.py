image=[[0,0,0],[0,1,0]]
sr=1
sc=1
newColor=2



col=len(image[0])
row=len(image)
visited=[[0 for c in range(col)] for r in range(row)]
_x=[0,0,1,-1]
_y=[1,-1,0,0]
q=[]
target=image[sr][sc]

#BFS
q.append([sr,sc])

while q:

    x,y=q.pop(0)
    image[x][y]=newColor

    for i in range(4):
        nx=x+_x[i]
        ny=y+_y[i]

        if 0<=nx<row and 0<=ny<col and image[nx][ny]==target and visited[nx][ny]==0:
            visited[nx][ny]=1
            q.append([nx,ny])

print(image)