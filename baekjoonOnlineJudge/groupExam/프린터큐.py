import sys
import heapq 
input=sys.stdin.readline

t=int(input())
for T in range(t):
    n,m=map(int,input().split())
    info=list(map(int,input().split()))
    arr=[]
    max_heap=[]
    for i in range(len(info)):
        arr.append([info[i],i])
        heapq.heappush(max_heap,-info[i])
    target=arr[0]
    idx=1
    answer=0
    priority_num=-heapq.heappop(max_heap)
    while 1:
        # print(target, p, arr, idx)

        if target[0]==priority_num and target[1]==m:
            answer+=1
            break

        if target[0] == priority_num: #제거
            priority_num=-heapq.heappop(max_heap)
            answer+=1
        else:
            arr.append(target) #못찾으면 뒤에 붙이기 

        target=arr[idx]
        idx+=1
    print(answer)
