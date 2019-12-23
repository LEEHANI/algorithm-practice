def solution(arr, divisor):
    answer = []

    for i in arr:
        if not i % divisor:
            answer.append(i)
    answer.sort()
    return answer if len(answer) != 0 else [-1]


print(solution([5, 9, 7, 10], 5))
