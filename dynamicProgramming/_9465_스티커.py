'''
dp 문제는 dp의 정의를 어떻게 하느냐가 중요하다 ! 

dp[i][0]: arr[i][0] 번째 스티커를 뗀다. arr[i][0]번째 스티커를 떼면 dp[i-1][1] 번째 스티커를 뗄수도 있고, 안뗄수도 있다.!  
dp[i][1]: arr[i][1] 번째 스티커를 뗀다. arr[i][1]번째 스티커를 떼면 dp[i-1][0] 번째 스티커를 뗄수도 있고, 안뗄수도 있다.! 
dp[i][2]: arr[i][0], arr[i][1] 번째 스티커를 떼지 않는다. 즉, 둘 다 안뗸다 ! 

dp[i][2]를 정의 안해줘서 삽질했었음 ..! 
'''

import sys

input = sys.stdin.readline

T = int(input())

for case in range(T):
    n = int(input())
    arr = [[0 for col in range(2)] for row in range(n)]
    dp = [[0 for col in range(3)] for row in range(n+1)]

    for i in range(2):
        info = list(map(int, list(input().split())))

        for j in range(n):
            arr[j][i] = info[j]

    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]
    dp[0][2] = 0

    for i in range(1, n):
        dp[i][0] = arr[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = max(dp[i-1][0], dp[i-1][1])

    print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
