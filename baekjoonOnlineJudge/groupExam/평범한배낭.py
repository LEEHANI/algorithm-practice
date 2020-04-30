'''
dp
'''
from itertools import combinations
import sys
input = sys.stdin.readline

arr=[]
n,k=map(int,input().split())
dp=[0]*(k+1)

for i in range(n):
    w,v=map(int,input().split())
    arr.append([w,v])
arr=sorted(arr, key=lambda x:(x[0]))

for i in range(n):
    # print(arr[i])
    target=arr[i][0]

    for j in range(1,(target+1)//2,1):
        dp[target]=max(dp[j]+dp[target-j], dp[target])
    dp[target]=max(dp[target],arr[i][1])

# print(dp)
start=arr[-1][0]+1
end=k+1
for i in range(start,end,1):
    for j in range(1,(i+1)//2,1):
        dp[i]=max(dp[j]+dp[i-j], dp[i])
# print(dp)
#     dic[w]=v

# for t in range(2,n+1):
#     for combination in combinations(dic.keys(),t):
#         if sum(combination) <= k:
#             temp=0

#             for num in combination:
#                 temp+=dic[num]
#             if answer<temp:
#                 answer=temp

print(dp[k])