def solution(x):
    if x%sum(list(map(int,list(str(x))))) == 0:
        return True
    return False

print(solution(10))
print(solution(12))
print(solution(13))