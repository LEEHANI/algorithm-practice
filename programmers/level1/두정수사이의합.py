def solution(a, b):
    if a==b:
        return a
    elif a>b:
        a,b=b,a
    return sum([i for i in range(a,b+1,1)])
print(solution(5,3))