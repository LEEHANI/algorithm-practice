from itertools import permutations

def solution(numbers):
    answer = ''
    n = len(numbers)
    numbers=list(map(str, numbers))
    print(n, numbers)
    # print(max([''.join(list(num)) for num in permutations(numbers, n)]))
    
    for num in permutations(numbers, n):
        print(num)
    # return max([''.join(list(num)) for num in permutations(numbers, n)])

# print(solution([6,10,2]))
print(solution([3,30,34,5,9]))