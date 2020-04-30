apartment=[[0 for i in range(15)] for j in range(15)]
for i in range(15):
    for j in range(1,15):
        if i==0:
            apartment[i][j]=j
        else:
            s=0
            for q in range(1,j+1):
                s+=apartment[i-1][q]
            apartment[i][j]=s
t=int(input())
for T in range(t):
    k=int(input())
    n=int(input())
    print(apartment[k][n])