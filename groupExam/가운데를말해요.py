'''
처음에 min_heap과 max_heap의 size를 같거나 1차이로 만들려는 시도는 좋았음 max_size <= min_size. 최대 1 차이
하지만 음수가 주어졌을 때 어떻게 할지까지는 생각하지 못했음. 음수가 있다는걸 안 순간 min_size <= max_size로 했었어야 함. 그 부분이 아쉽. 한쪽으로만 생각했음 
또, max_heap_top > min_heap_top일 경우를 사이즈 차이가 났을 때만 발생할거라고 생각했는데.. 사이즈가 같을떄도 발생할 수 있다는걸 생각하지 못했음.

결론적으로 한쪽으로만 생각하지 말고, 사이즈가 같을 경우에도 데이터가 다를 수 있다는 걸 인지하자

'''
import heapq
import sys
input=sys.stdin.readline

mi_heap=[]
mx_heap=[]
mi_size=0
mx_size=0
mi_top=0
mx_top=10001

n=int(input())

for i in range(1,n+1):
    num=int(input())

    heapq.heappush(mx_heap,-num)
    mi_top=num
    if i%2==0:
        heapq.heappush(mi_heap,-heapq.heappop(mx_heap))
        mi_size+=1
    else:
        mx_size+=1

    if mi_heap and mx_heap:

        mi_top=heapq.heappop(mi_heap)
        mx_top=-heapq.heappop(mx_heap)

        if mi_top < mx_top:
            heapq.heappush(mi_heap, mx_top)
            heapq.heappush(mx_heap, -mi_top)
        else:
            heapq.heappush(mi_heap, mi_top)
            heapq.heappush(mx_heap, -mx_top) 

    mx_top=-heapq.heappop(mx_heap)
    print(mx_top)
    heapq.heappush(mx_heap, -mx_top)
