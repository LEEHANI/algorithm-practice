def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        answer.append(list(sorted(arr[i-1:j]))[k-1])
    return answer


arr = [1, 5, 2, 6, 3, 7, 4]
commands = []
commands.append([2, 5, 3])
commands.append([4, 4, 1])
commands.append([1, 7, 3])
solution(arr, commands)
