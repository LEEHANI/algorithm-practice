'''
https://programmers.co.kr/learn/courses/30/lessons/42626
'''
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while 1:
        low_number = heapq.heappop(scoville)
        
        if low_number >= K:
            break
        try:
            heapq.heappush(scoville, (low_number + (heapq.heappop(scoville)*2)))
        except IndexError as identifier:
            return -1
        answer +=1
    return answer

# print(solution([1,2,3,9,10,12], 7))
print(solution([0,1], 3))