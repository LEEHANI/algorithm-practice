def solution(n):
    # str_n = str(n)
    # return [int(str_n[-(i+1)]) for i in range(len(str_n))]
    return list(map(int, reversed(str(n))))
print(solution(12345))