def solution(arr):
    answer = []

    answer.append(arr[0])

    for i in range(1, len(arr), 1):
        if answer[-1] == arr[i]:
            continue
        answer.append(arr[i])
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]

print(solution(arr))
