n = int(input())
arr = [input() for _ in range(n)]

answer = ''

for i in range(len(arr[0])):
    target = arr[0][i]
    flag = 1
    for j in range(1, n, 1):
        if target != arr[j][i]:
            answer = answer + '?'
            flag = 0
            break
    if flag:
        answer = answer + target

print(answer)
