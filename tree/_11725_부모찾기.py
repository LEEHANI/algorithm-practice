'''
문제를 봤을 때 가장 처음 든 생각: 입력받는 애가 부모인지 자식인지 어캐 구분짓지?
트리 생성 5번 방법인, A[i][0] A[i][1]를 이용해 짜다가 막혔다. 이게 이진트리인지 아닌지 판단도 하지 않고 알고리즘을 짜려했기 때문이다.

문제를 이해하고 나서, 어떤 방법으로 짤건지 생각부터 하자 !

이 문제는 이진 트리가 아니기 때문에 트리 생성 5번 방법이 아니라 방법1(인접 배열), 방법2(인접리스트)를 사용해 데이터를 저장해야한다. 
방법1는 메모리를 낭비하니, 방법2로 선택하자.
예제 1번의 연결 정보를 인접 리스트에 저장해보자.
[[], [4, 6], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
노드 1번이랑 연결되어있는 노드는 4,6번이다. 루트 노드가 1번이므로 4, 6는 자식노드이다. visited에 4, 6번 노드에 부모 노드를 저장해놓는다. [-1, 0, -1, -1, -1, 1, -1, -1]
그 다음 1번의 첫번째 자식인 4번을 부모노드로 놓는다(Queue). 자식노드 [1, 2, 7]에서 부모노드가 없는 자식을 찾아 부모 visited에 부모노드 4를 저장해놓는다. [-1, 0, 4, -1, -1, 1, -1, 4]

주의해야 할 점은 visited를 먼저 체크하고 queue에 넣을 것 

트리도 결국은 그래프이기 때문에 이 문제는 DFS, BFS 문제이기도 했다..
'''
from collections import deque
import sys
sys.setrecursionlimit(10**7)  # DFS는 stackoverflow 가 발생하니 limit 크기 늘려주기 !

input = sys.stdin.readline
N = int(input())


def DFS(parent):
    for i in arr[parent]:
        if(visited[i] == -1):
            visited[i] = parent
            DFS(i)


def BFS(start):
    q = deque()
    visited[start] = 0  # 1번
    q.append(start)

    while q:
        parent = q.popleft()

        for child in arr[parent]:
            if visited[child] == -1:
                visited[child] = parent
                q.append(child)


arr = [[] for _ in range(N+1)]
visited = [-1]*(N+1)  # 방문했으면 부모노드로 저장
visited[1] = 0

# 입력
for i in range(N-1):
    n, m = map(int, input().split())

    arr[n].append(m)
    arr[m].append(n)

# 알고리즘
DFS(1)

# 출력
for i in visited[2:]:
    print(i)
