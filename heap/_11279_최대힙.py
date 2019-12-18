import sys

input = sys.stdin.readline


def push(x):
    max_heap.append(x)
    push_heapify(len(max_heap)-1)


def pop():

    try:
        print(max_heap[1])
        max_heap[1] = max_heap[-1]
        max_heap.pop(-1)
        pop_heapify()
    except:
        print(0)


def pop_heapify():
    parent = 1

    while 1:
        try:
            child1 = parent*2

            if len(max_heap) > parent*2+1:
                child2 = parent*2+1
            else:
                child2 = 0

            max_child = child1 if max_heap[child1] > max_heap[child2] else child2

            if max_heap[parent] < max_heap[max_child]:
                max_heap[parent], max_heap[max_child] = max_heap[max_child], max_heap[parent]
                parent = max_child
            else:
                break
        except:
            break
            # pass


def push_heapify(child):

    parent = child//2

    while child > 1:

        if max_heap[parent] < max_heap[child]:
            # swap
            max_heap[parent], max_heap[child] = max_heap[child], max_heap[parent]

            child = parent
            parent = child//2
        else:
            break


N = int(input())
max_heap = [-1]

for i in range(N):
    x = int(input())

    if x:
        push(x)
    else:
        pop()
