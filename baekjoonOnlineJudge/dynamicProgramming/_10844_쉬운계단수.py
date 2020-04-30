'''
dp[n][m] := 길이가 n인 계단수 개수 , n일때 계단 수의 개수는 m

- 길이가 2일 때를 생각해보자
     1 0
1 2  2 1
2 3  3 2
3 4  4 3
4 5  5 4
6 7  7 6
8 9  9 8

0, 9 를 제외하고는 2개씩 나온다. 
끝의 자리가 5라면 45, 65이다. 즉, 끝자리 보다 숫자 하나가 적거나, 큰 경우 이므로 2가지가 나온다.

'''
n = int(input())
dp = [[0 for row in range(10)] for col in range(n)]

# 초기화
for i in range(1, 10, 1):
    dp[0][i] = 1

answer = 0

for i in range(1, n, 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

for i in range(10):
    answer += dp[n-1][i]

print(answer % 1000000000)
