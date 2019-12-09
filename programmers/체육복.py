'''
[주의해야할 점]
1. 제한조건을 끝까지 읽어보기
2. 어느 조건으로 먼저 걸러야할지 생각해보기
3. for문에서 remove를 했을 시 인덱스 문제가 발생할 가능성 다분
'''


def solution(n, lost, reserve):
    answer = n-len(lost)
    lost.sort()
    reserve.sort()

    # for target in lost:
    i = 0
    while i < len(lost):
        if reserve.count(lost[i]):
            reserve.remove(lost[i])
            lost.remove(lost[i])

            answer += 1
            continue
        i += 1

    for target in lost:
        for cloth in reserve:
            if cloth == target-1 or cloth == target+1:
                reserve.remove(cloth)
                answer += 1
                break

    return answer


lost = [1]
reserve = [1, 2]
print(solution(5, lost, reserve))
