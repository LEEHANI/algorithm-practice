n=25


tribonacci=[0]*(n+1)
tribonacci[1]=1
tribonacci[2]=1

for i in range(3,n+1):
    tribonacci[i]=tribonacci[i-3]+tribonacci[i-2]+tribonacci[i-1]
    
print(tribonacci[n])