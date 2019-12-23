def solution(n):
    result = [ i for i in range(1,n//2+1,1) if n%i == 0]
    return sum(result)+n
print(solution(36))