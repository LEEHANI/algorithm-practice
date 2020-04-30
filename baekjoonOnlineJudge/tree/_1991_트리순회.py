import sys


def preorder(start):

    if start < 0:
        return

    print(chr(start+ord("A")), end="")
    preorder(arr[start][0])
    preorder(arr[start][1])


def inorder(start):

    if start < 0:
        return

    inorder(arr[start][0])
    print(chr(start+ord("A")), end="")
    inorder(arr[start][1])


def postorder(start):

    if start < 0:
        return

    postorder(arr[start][0])
    postorder(arr[start][1])
    print(chr(start+ord("A")), end="")


N = int(sys.stdin.readline())

arr = [[0 for col in range(2)] for row in range(N)]

for i in range(N):
    a, b, c = sys.stdin.readline().split()

    a = ord(a)-ord('A')

    if b == ".":
        b = -1
    else:
        b = ord(b)-ord('A')

    if c == ".":
        c = -1
    else:
        c = ord(c)-ord('A')

    arr[a][0] = b
    arr[a][1] = c

preorder(0)
print()
inorder(0)
print()
postorder(0)
print()
