def solution(prices):
    answer = [0]*len(prices)
    s=len(prices)
    for i in range(s):
        target=prices[i]
        for j in range(i+1, s, 1):
            if target <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer
print(solution([1,2,3,2,3]))