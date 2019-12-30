def solution(n):
    memoization=[0]*(n+1)
    memoization[1]=1
    
    for i in range(2,n+1,1):
        memoization[i]=memoization[i-1]+memoization[i-2]
    
    return memoization[n]%1234567
print(solution(3))
print(solution(5))