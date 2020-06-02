import math
n=13

def dfs(start):
    q=[[start,0]]

    while q:
        
        N,depth=q.pop(0)

        # N은 sqrt(N)을 사용할 수 있다. 
        # 즉, 13이면 sqrt(13)=3.xxx이니 1,2,3의 제곱수를 사용할 수 있다. 
        size=int(math.sqrt(N))

        for i in range(size,0,-1):
            # N = N-(1*1), N-(2*2), N-(3*3)
            temp=int(N-i**2)

            if temp == 0:
                return depth+1

            q.append([temp,depth+1])

def dp(n):
    dp=[99999999999]*(n+1)
    dp[0]=0
    squares=[]

    for i in range(1,n+1):
        if int(math.sqrt(i))**2==i:
            dp[i]=1
            squares.append(i)
        else:
            for square in squares:
                # dp[i]를 더 작은 dp[j]로 놓고 생각해보자 
                # dp[i]는 sqrt(i)를 사용할 수 있다. 
                # dp[i] = dp[square] + dp[i-square]
                # min(dp[1]+dp[11], dp[4]+dp[8], dp[9]+dp[3])
                if dp[i]>dp[square]+dp[i-square]:
                    dp[i]=dp[square]+dp[i-square]
    return dp[n]

print(dp(n))
print(dfs(n))