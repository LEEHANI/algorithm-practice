'''
1. m*n 행렬 x n*r 행렬 == m*r 행렬
2. m*r 행렬 c[i][j] == (a[i][0] * b[0][j]) + (a[i][1] * b[1][j]) + (a[i][2] * b[2][j]) + ... + (a[i][n-1] * b[n-1][j])
   즉, c[i][j] == sum(a[i][k]*b[k][j]), k=0 to n-1
3. 예시보단 일반화 !! 
'''
def solution(arr1, arr2):
    
    m=len(arr1)
    n=len(arr1[0])
    r=len(arr2[0])
    answer=[[0 for col in range(r)] for row in range(m)]
    for i in range(m):
        for j in range(r):
            answer[i][j] = sum([arr1[i][k]*arr2[k][j] for k in range(n)])
    return answer

print(solution([[1,4],[3,2],[4,1]],[[3, 3], [3, 3]]))