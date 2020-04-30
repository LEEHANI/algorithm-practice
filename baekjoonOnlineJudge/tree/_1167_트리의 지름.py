'''
[문제 풀기 전 내 생각]
1. 1번 노드를 시작지점으로 놓고 bfs탐색 하면 되겠지 .. => 틀림. 1번부터 시작하는 게 가장 긴 거리가 아님
2. 각 노드를 시작 지점으로 놓고 탐색 후 가장 긴 노드를 출력 => 시간초과. O(N^2) 복잡도 .. 
3. 단말 노드만 탐색하면 되겠지 => 시간초과. 최악의 경우 O(N^2) 복잡도(?) .. 

[알고리즘]
긴 거리를 구하기 위해서는 양 끝의 노드를 알면 된다. 근데 잘 생각해 보면 한쪽 끝만 알면 된다. 
한쪽 끝을 알면 bfs 탐색으로 다른 끝을 알 수 있기 때문이다. 한쪽 끝을 알면 다른 끝을 찾아가면서 거리를 재면 되니 사실상 문제가 해결된 셈이다.

1. 한쪽 끝을 알기 위해서는 우선 임의의 노드를 출발지로 정하고 bfs 탐색을 한다. 
   (임의의 노드를 출발지로 선정해도 되는 이유는 트리이기 때문이다. 트리는 사이클이 없다는 조건이 깔려있기 때문에, 시작 노드를 임의의 노드로 해도 bfs 탐색을 하면 끝에 노드를 알 수 있다. )
2. 1번 탐색으로 얻은 끝 노드를 시작점으로 놓고 bfs 긴 거리를 찾기 위해 탐색을 한다. 

[내가 주의해야 할 점]
정점이 순서대로 들어오지 않을 수 있다 ! 제발 예시 대로 입력이 주어질거라고 생각하지 말자 ...
'''


import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    global global_node

    max = 0

    q = deque()
    visited[start] = 1
    q.append((start, 0))

    while q:
        node, distance = q.popleft()

        if max < distance:  # 지름이 길 떄
            global_node = node
            max = distance

        for child in arr[node]:
            n, d = child

            if visited[n] == -1:
                visited[n] = 1
                q.append((n, distance+d))
    return max


# 입력
V = int(input())

# 메모리
arr = [[] for _ in range(V+1)]

# 입력
for v in range(V):
    info = list(map(int, list(input().split())))

    node = info[0]

    for i in range(1, len(info)-1, 2):
        if info[i] != -1:
            arr[node].append((info[i], info[i+1]))

answer = 0
global_node = 0

# 1번째 bfs
# 목표 : 거리가 가장 먼 노드 찾기
visited = [-1]*(V+1)
result = bfs(1)

if answer < result:
    answer = result

# 2 번째 bfs
# 목표 : 거리가 먼 노드를 시작 노드로 지정해놓고 가장 긴 거리 찾기
visited = [-1]*(V+1)
result = bfs(global_node)

if answer < result:
    answer = result

print(answer)
