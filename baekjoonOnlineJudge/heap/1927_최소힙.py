import heapq
import sys

input = sys.stdin.readline

n=int(input())
min_heap=[]

for i in range(n):
    x=int(input())

    if x==0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, x)