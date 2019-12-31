'''
dp[i][j] := i번째에서, j번째 열을 택했을 때 가질수 있는 최댓값.
'''
def solution(land):
    n=len(land)
    dp = [[0 for col in range(4)] for row in range(len(land))]
    dp[0]=land[0]
    for i in range(1,n,1):
        j=i-1
        # print(max(land[j][1], land[j][2], land[j][3]), 
        #       max(land[j][0], land[j][2], land[j][3]),
        #       max(land[j][0], land[j][1], land[j][3]),
        #       max(land[j][1], land[j][1], land[j][2]))
        dp[i][0]+=max(dp[j][1], dp[j][2], dp[j][3])+land[i][0]
        dp[i][1]+=max(dp[j][0], dp[j][2], dp[j][3])+land[i][1]
        dp[i][2]+=max(dp[j][0], dp[j][1], dp[j][3])+land[i][2]
        dp[i][3]+=max(dp[j][0], dp[j][1], dp[j][2])+land[i][3]
    return max(dp[n-1])

# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
# print(solution([[1,2,4,3],[1,2,6,4],[1,2,7,3]])) # 15
# print(solution([[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
# print(solution([[1,1,1,1],[1,2,1,1],[1,100,1,1]])
print(solution([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
# print(solution([[1, 2, 2, 2], [100, 100, 1, 100], [100, 1, 1, 1]])) # 202