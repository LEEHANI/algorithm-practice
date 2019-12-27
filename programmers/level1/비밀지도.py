def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a1,a2=bin(arr1[i])[2:].zfill(n), bin(arr2[i])[2:].zfill(n)
        value=''
        for j in range(n):
            if a1[j]=='1' or a2[j]=='1':
                value+="#"
            else:
                value+=" "
        answer.append(value)
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))