A=[['W','B'],['B','W']]
B=[['B','W'],['W','B']]
N,M=map(int,input().split())
arr=[]
answer=100
for i in range(N):
    arr.append(list(input()))

for n in range(0,N-7):
    for m in range(0,M-7):
        a,b=0,0 
        for i in range(n,n+8):
            x=i%2
            for j in range(m,m+8):
                target=arr[i][j]

                y=j%2
                if target!=A[x][y]:
                    a+=1
                if target!=B[x][y]:
                    b+=1
        answer=min(a,b,answer)
print(answer)

