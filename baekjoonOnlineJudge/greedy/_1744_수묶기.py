'''

어떻게 하면 값을 최대로 만들 수 있을까?

[-7, -5, -1, 0, 1, 5, 10]
(-7, -5), -1, 0, 1, (5, 10) 큰 수끼리 묶는다. 그리고 묶이지 않는 애들은 다 더해준다.
근데 아니다 !!! 0이 있을 땐 (-1, 0)로 묶어주면 음수를 0으로 바꿀 수 있다. 
그러니 0이 존재할 때를 고려해야한다. 

[알고리즘]
1. 정렬
2. 음수끼리 묶기 
3. 양수끼리 묶기
4. 묶이지 않은 나머지들 처리하기
  1) 0이 존재하고 음수가 존재하면 0으로 처리
  2) 그렇지 않으면 그냥 더해주기

[내가 실수한 점]
하지만 여기서 끝난게 아니다............ 
1. 같은 수가 중복되서 나올 수 있다. [-5, -1, -1, 0, 0, 1, 1, 5] 가 가능
2. (1, n)은 곱하면 n임. 최대값을 구하기 위해서는 1+n을 해줘야 한다.!!! 1이 나올 경우를 조심해야함. 양수일 때만 고려 


[-3, -2, -1, 0, 1, 2, 3]
case 1: 0이 존재
큰 양수끼리 두 개 묶기
0은 가장 가까운 마이너스와 묶기
작은 음수끼리 두 개 묶기

[-3, -2, -1, 1, 2, 3]

case 2: 0이 존재 x
큰 양수끼리 두 개 묶기
작은 음수끼리 두 개 묶기
나머지는 더하기

test case
3 [-1 -3 -2] 5
3 [-1, -2, 10] 12
4 [-1, -2, 10, 2] 22
3 [-1, 10, 5] 49
4 [1, 2, 3, 4] 14
3 [1, 3, 4] 13

[-1 0 10] 10
[-1 -2 0] 2
[-1 0 1] 1
4 [-1 -2, 0, -5] 10
'''
N = int(input())
arr = [0]*(N)
visited = [0]*(N)

for i in range(N):
    arr[i] = int(input())

arr.sort()

answer = 0
minus_break = 0

# 음수 묶기
for i in range(0, N, 2):
    try:
        if arr[i] < 0 and arr[i+1] < 0:

            answer += arr[i]*arr[i+1]

            visited[i] = 1
            visited[i+1] = 1
        else:
            minus_break = i
            break
    except IndexError:
        minus_break = i
        pass

# 양수 묶기
for i in range(N-1, 0, -2):
    try:
        if arr[i] > 0 and arr[i-1] > 0:

            if arr[i] == 1 or arr[i-1] == 1:
                answer += arr[i] + arr[i-1]
            else:
                answer += arr[i]*arr[i-1]

            visited[i] = 1
            visited[i-1] = 1
        else:
            break
    except IndexError:
        pass


visited_sum = 0

# 묶고 난 나머지 애들 처리하기
for i in range(minus_break, N, 1):
    if not visited[i]:
        if visited_sum < 0 and arr[i] == 0:
            visited_sum = 0
        else:
            visited_sum += arr[i]

print(answer + visited_sum)
