'''
dp[i][0] i번째일 때, 선택 안함
dp[i][1] i번째일 때, 한잔 마심 
dp[i][2] i번째일 때, 두잔째 마시는중 
'''
import sys
# input = sys.stdin.readline

n=int(input())
dp=dp = [[0 for col in range(3)] for row in range(n+1)]
info=[]
for i in range(n):
    temp=input()
    info.append(temp)
info=list(map(int,info))

dp[0][0]=0
dp[0][1]=info[0]
dp[0][2]=info[0]
for i in range(1,n):
    dp[i][0] =max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] =info[i]+dp[i-1][0]
    dp[i][2] =dp[i-1][1]+info[i]
print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))