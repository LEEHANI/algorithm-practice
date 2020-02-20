def solution(brown, red):
    brown=brown-4
    divisor=[1]

    # 약수 구하기
    for i in range(2,red//2+1):
        if red%i == 0:
            divisor.append(i)

    for i in divisor:
        a=i
        b=red//i

        if a*2+b*2 == brown:
            return [max(a,b)+2,min(a,b)+2]


# print(solution(10,2))
# print(solution(8,1))
# print(solution(24,24))