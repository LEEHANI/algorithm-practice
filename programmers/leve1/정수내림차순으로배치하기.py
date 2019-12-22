def solution(n):
    return int(''.join(reversed(sorted(str(n)))))
print(solution(118372))