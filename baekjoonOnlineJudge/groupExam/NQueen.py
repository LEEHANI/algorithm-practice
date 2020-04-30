n=int(input())
# n=12
answer=0
arr=[[0 for i in range(n)] for j in range(n)]
visited=[0]*n
visited1=[0]*(1000) # /
visited2=[0]*(1000) # \

def check(x,y):
    if visited1[x+y]==1:
        return False
    if visited2[x+n-1-y]==1:
        return False
    return True

def recursive(depth,q,n):
    global answer

    if depth==n:
        if q==n:
            answer+=1
        return
    else:
        for j in range(n):
            if visited[j] == 0 and check(depth,j):
                visited[j]=1
                visited1[j+depth]=1
                visited2[depth+n-1-j]=1
                arr[depth][j]=1

                recursive(depth+1,q+1,n)

                visited[j]=0
                visited1[j+depth]=0
                visited2[depth+n-1-j]=0
                arr[depth][j]=0

recursive(0,0,n)
print(answer)


