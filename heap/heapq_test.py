'''
heapq의 순서는 정렬된 값이 아니다 !! 
heapq == 우선순위 큐 

heapq는 heap의 라이브러리 
heapq 라이브러리의 default는 min_heap 이다 
max_heap을 사용하고 싶으면 item에 - 붙이기
'''
import heapq

min_heap = []
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 2)

print(min_heap)
print(heapq.heappop(min_heap))


max_heap = []
heapq.heappush(max_heap, -7)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -2)

print(max_heap)
print(-heapq.heappop(max_heap))
