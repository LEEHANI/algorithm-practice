'''
계차수열의 이해가 필요한 문제

n이 속하는 구역 찾음
벌집 모양이기 떄문에 그 구역만 찾으면 최단거리임 

시간초과 이유 
구역을 6개로 나눴는데 한 구역은 다른 케이스가 발생
ex) 22~25, 25~28, 28~31, 31~34, 34~37, 22 ~ 37
'''
n=int(input())
arr=[0,1,2,3,4,5,6,7] # 각 구역의 수 
#   0 1 2 3 4 5 6 7
dd=[0,0,1,2,3,4,5,6] #각 구역마다 6씩 계차수열 증가 
answer=1
def find_answer(n):
    global answer 

    if n==1:
        return 1

    while 1:
        answer+=1

        for j in range(1,7):
            if arr[j]<=n<=arr[j+1]:
                return answer

        arr[1]=arr[7]+1
        for j in range(2,8):
            dd[j]+=6
            arr[j]+=dd[j]

print(find_answer(n))