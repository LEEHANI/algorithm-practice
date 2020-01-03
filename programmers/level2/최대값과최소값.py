def solution(s):
    arr=list(map(int, s.split()))
    return str(min(arr))+" "+str(max(arr))
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))