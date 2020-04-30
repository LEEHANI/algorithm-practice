'''
1차원 dp로는 문제가 해결 되지 않는다.
그럴 땐 2차원 dp로 생각해보자.

dp[n][m] := 길이가 n인 오르막의 개수, 마지막 숫자는 m

- 길이가 2일 때를 생각해보자
dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1
dp[0][3] = 1
...
dp[0][8] = 1
dp[0][9] = 1

dp[1][0] = dp[0][0]
dp[1][1] = dp[0][0:1]
dp[1][2] = dp[0][0:2]
...
dp[1][8] = dp[0][0:8]
dp[1][9] = dp[0][0:9]


1. 길이가 1일 때는 초기값 1로 셋팅 해줘야함
2. 길이가 n일 때는 dp[n-1][0:m]

'''
n = int(input())
dp = [[0 for row in range(10)] for col in range(n)]


answer = 0

# 초기화
for i in range(10):
    dp[0][i] = 1

# 알고리즘
for i in range(1, n, 1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]  # 0부터 k까지 더하기
            dp[i][j] %= 10007

# 답 구하기
for i in range(10):
    answer += dp[n-1][i]

print(answer % 10007)
