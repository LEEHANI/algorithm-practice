'''
최단 경로는 BFS를 이용해 풀자

'''

from collections import deque
import sys

# def dfs(x, y, answer):
#     global real_answer

#     for i in range (N):
#         print(visited[i])
#     print(answer)
#     print()

#     if(x == N-1 and y == M-1):
#         real_answer = answer
#         return answer

#     for i in range (4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if(0 <= nx < N and 0 <= ny < M): # 파이썬의 장점! if(nx >= 0 & ny >= 0 & nx < N & ny < M)
#             if(arr[nx][ny] == 1 and visited[nx][ny] == 0):
#                 visited[x][y] = 1
#                 dfs(nx, ny, answer + 1)


def bfs(x, y):
    q = deque()
    visited[x][y] = 1
    q.append((x, y, 1))

    while q:
        x, y, cnt = q.popleft()

        if(x == N-1 and y == M-1):
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < N and 0 <= ny < M):
                if(arr[nx][ny] == '1' and visited[nx][ny] == 0):
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt+1))


# 입력
N, M = map(int, sys.stdin.readline().strip().split())
arr = []
visited = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    arr.append(list(sys.stdin.readline()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# dfs(0, 0, 1)
# 알고리즘 + 출력
print(bfs(0, 0))
