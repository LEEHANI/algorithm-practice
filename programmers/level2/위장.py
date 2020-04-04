from itertools import combinations

'''
모자: [yellow_hat, green_turban] 
마스크: [mask1, mask2]
어룰: [makeup1]

모자의 종류가 [yellow_hat, green_turban] 라면, 
yellow_hat를 택한경우, green_turban를 택한경우, 아무것도 택하지 않은 경우가 나오므로 모자의 경우의 수는 3이다. [yellow_hat, green_turban, X]

[yellow_hat, green_turban, X]
[mask1, mask2, X]
[makeup1, X]
이를 다른 종류와의 경우의 수를 생각해보면 3x3x2이 된다.
근데 아무것도 선택하지 않는 경우도 포함되어 있으므로 마지막에 -1을 해줘야한다.  
'''
def solution(clothes):
    answer = 1

    info={}

    for v,k in clothes:
        if k in info.keys():
            info[k] = info[k]+1
        else:
            info[k]=2

    # 시간 초과
    # for n in range(2, len(info.values())+1):
    #     for i in combinations(info.values(), n):
    #         temp=1
    #         for j in i:
    #             temp*=j
    #         answer += temp

    for i in info.values():
        answer *= i

    answer = answer-1
    return answer

# solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])
print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear'],  ['green_turban1', 'mask'],  ['green_turban2', 'mask']]))
# solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']])

