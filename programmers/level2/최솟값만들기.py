def solution(A,B):
    answer = 0

    A=sorted(A)
    B=sorted(B, reverse=True)
    size=len(A)
    
    for i in range(size):
        answer+=A[i]*B[i]
    
    return answer
# print(solution([1,4,2],[5,4,4]))
print(solution([1,2],[3,4]))