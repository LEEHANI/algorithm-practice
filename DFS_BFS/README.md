
# DFS, BFS
- DFS(Depth First Search, 깊이 우선 탐색)는 Stack을 이용한 탐색 기법
  + 한 정점으로만 나아간다
  + O(V+E)
- BFS(Breadth First Search, 너비 우선 탐색)는 Queue를 이용한 탐색 기법
  + 모든 정점으로 나아간다. 
  + O(V+E)

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

```python
# 그래프 탐색
def DFS(start):
    for i in arr[start]:
        if not visited[i]:
            visited[start] = 1
            DFS(i)
```
```python
# 백트래킹
def DFS(start):
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            DFS(i)
            visited[i] = 0
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