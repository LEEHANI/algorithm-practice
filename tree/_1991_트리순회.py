import sys  # 입력

# 전위 순회 (루트)(왼쪽 자식)(오른쪽 자식)


def preorder(start):

    if 0 <= start < 26:
        return

    print(chr(start+ord("A")), end="")
    preorder(arr[start][0])
    preorder(arr[start][1])

# 중위 순회 (왼쪽 자식)(루트)(오른쪽 자식)


def inorder(start):

    if 0 <= start < 26:
        return

    inorder(arr[start][0])
    print(chr(start+ord("A")), end="")
    inorder(arr[start][1])

# 후위 순회(왼쪽 자식)(오른쪽 자식)(루트)


def postorder(start):

    if 0 <= start < 26:
        return

    postorder(arr[start][0])
    postorder(arr[start][1])
    print(chr(start+ord("A")), end="")


# 입력
N = int(sys.stdin.readline())
arr = [[-1 for col in range(2)] for row in range(N)]

for i in range(N):
    # p, c1, c2 = sys.stdin.readline().split()

    # p = ord(p)-ord('A')
    # if c1 != ".":
    #     c1 = ord(c1)-ord('A')
    # if c2 != ".":
    #     c2 = ord(c2)-ord('A')
    p, c1, c2 = map(lambda x: ord(x)-ord('A'),
                    sys.stdin.readline().split())  # [A,B,C]

    arr[p][0] = c1
    arr[p][1] = c2

# 출력
preorder(0)
print()
inorder(0)
print()
postorder(0)
print()
