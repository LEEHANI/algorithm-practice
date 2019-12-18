
def bubble_sort(reverse):
    for i in range(len(arr)-1):
        for j in range(i, len(arr), 1):
            a, b = arr[i], arr[j]

            if reverse:
                if b > a:
                    arr[i], arr[j] = b, a
            else:
                if a > b:
                    arr[i], arr[j] = a, b

        print(arr)


arr = list(map(int, list(input())))
arr.sort(reverse=True)
for i in arr:
    print(i, end="")

# bubble_sort()
