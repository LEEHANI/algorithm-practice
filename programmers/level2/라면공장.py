'''
CASE 11 실패 solution(4,[4],[26],30) 일때 
if size==i+1:
    q.append(supplies[i])
해야함
'''
import heapq as hq

def solution(stock, dates, supplies, k):
    answer = 0
    
    size=len(dates)
    q=[]
    
    for i in range(len(dates)):
        
        # 마지막 공급일날
        if size==i+1:
            hq.heappush(q,-supplies[i])
            q.sort()
            
            # K일까지 버틸수없으면
            while stock < k:
                if len(q)==0:
                    break
                stock += -hq.heappop(q)
                answer+=1
        
            return answer
        
        # 다음 공급일까지 버틸수 있으면
        if stock >= dates[i+1]:
            hq.heappush(q,-supplies[i])
            continue
        # 버틸 수 없으면 공급받을 수 있는 밀가루 중 최대값 공급받기
        else:
            hq.heappush(q,-supplies[i])
            q.sort()
            stock += -hq.heappop(q)
            
            answer+=1
    
    return answer

# print(solution(4,[4,10,15],[20,5,10],30))
print(solution(4,[4],[26],30))
# print(solution(10,[5, 10],[1, 100],100))
# print(solution(2,[1],[10],10))
# print(solution(4,[1,2,3,4],[10,40,30,120],100))

# print(sorted([10,40,20]))