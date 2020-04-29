n=int(input())
link=int(input())

def dfs(start):
    global answer 

    visited[start]=1
    for i in range(1,n+1):
        if arr[start][i]==1 and visited[i]==0:
            dfs(i)
            answer+=1

visited=[0]*(n+1)
arr=[[0 for i in range(n+1)] for i in range(n+1)]
answer=0

for i in range(link):
    x,y=input().split()
    x=int(x)
    y=int(y)
    arr[x][y]=1
    arr[y][x]=1
dfs(1)
print(answer)

