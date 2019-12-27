def solution(n, m):
    a,b=max(n,m),min(n,m)
    mod=a%b
    while mod>0: # 유클리드 호제법 
        a,b=b,mod 
        mod=a%b
    return [b, n*m//b]

print(solution(3,12))
print(solution(2,5))