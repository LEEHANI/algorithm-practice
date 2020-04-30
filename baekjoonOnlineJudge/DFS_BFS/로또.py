def dfs(depth, start, result):
    global k

    if depth == 6:
        for i in range(6):
            print(result[i],end=' ')
        print()
        return 

    for i in range(start, k):
        result[depth]=t[i+1]
        dfs(depth+1, i+1, result)


while 1:
    t=list(map(int,input().split()))

    if t[0]==0:
        break

    k=t[0]
    visited=[0]*(k+1)
    result=[0]*(6)

    dfs(0, 0, result)
    print()



