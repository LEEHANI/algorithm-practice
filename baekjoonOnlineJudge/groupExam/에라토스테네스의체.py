n,k=map(int,input().split())

def eratosthenes(n,k):
    arr=[i for i in range(n+1)]
    p=2
    answer=0
    for i in range(2,n+1):
        if arr[i]==0:
            continue
        else:
            p=i

            for j in range(p, n+1, p):
                if arr[j]==0:
                    continue
                arr[j]=0
                answer+=1
                if answer==k:
                    print(j)
                    break
eratosthenes(n,k)