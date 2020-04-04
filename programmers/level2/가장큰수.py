from itertools import permutations

def solution(numbers):
    answer = ''
    # n = len(numbers)
    # numbers=list(map(str, numbers))
    # print(max([''.join(list(num)) for num in permutations(numbers, n)]))
    
    arr=[]
    for num in numbers:
        arr.append((int((str(num)*4)[0:4]),num))
    arr=sorted(arr, key=lambda x: (x[0]), reverse=True)
    print(arr)
    return str(int(''.join(str(j) for i,j in arr)))


# print(solution([6,10,2]))
# print(solution([3,30,34,5,9]))
print(solution([0, 0]))