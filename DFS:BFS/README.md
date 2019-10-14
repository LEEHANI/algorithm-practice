


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
```
def DFS(start):
    visited[start] = 1

    for i in arr[start]:
        if not visited[i]:
            DFS(i)
```