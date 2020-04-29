'''
조합
'''
from itertools import combinations

n,m=map(int,input().split())
arr=list(map(int,input().split()))
answer=0
for i in combinations(arr,3):
    target=sum(i)

    if target <= m and answer<target:
        answer=target

print(answer)