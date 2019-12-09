n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

arr = [[-1 for col in range(2)] for row in range(n)]

print(in_order)
print(post_order)

# for i in arr:

print(arr)


def tree_in_order(start):
    print(start, arr)

    if start == n:
        return
    tree_in_order(arr[start][0])
    print(in_order.pop())
    # arr[start][0] = in_order.pop()
    tree_in_order(arr[start][1])
    # arr[start][0] = n_order.pop()


tree_in_order(0)
print(arr)
