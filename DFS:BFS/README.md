
# DFS, BFS
DFS(Depth First Search, 깊이 우선 탐색)는 Stack을 이용한 탐색 기법
BFS(Breadth First Search, 너비 우선 탐색)는 Queue를 이용한 탐색 기법

### 1차원

BFS
```
from collections import deque

def BFS(start):
    q = deque()
    visited[start] = 1
    q.append(start)

    while q:
        v = q.popleft()

        for i in arr[v]:
            if not visited[i]: # if visited[i] == 0 
                visited[i] = 1
                q.append(i)
```

DFS
- recursive
```
def DFS(start):
    visited[start] = 1

    for i in arr[start]:
        if not visited[i]:
            DFS(i)
```
- iterative


### 2차원
엣지의 방향이 존재함 
```
def DFS(x, y):
    visited[x][y] = true

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and arr[nx][ny] and not visited[nx][ny]:
            DFS(nx, ny)

```