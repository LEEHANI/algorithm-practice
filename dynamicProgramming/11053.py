'''
dp[i] = arr[i]로 끝나는 가장 긴 증가하는 부분 수열의 갯수 
'''
n=6
info=[0,10,20,10,30,20,50]

# n=int(input())
# info=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=1
    for j in range(1,i):
        if info[j]<info[i] and dp[i]<dp[j]+1:
            dp[i] = dp[j]+1
    print(dp)

print(max(dp))