'''
from itertools import combinations
'''
from itertools import combinations
def solution(nums):
    global answer
    answer=0
    
    # solution1
    # n_and_m(0, 0, nums, [0,0,0]) 
    
    # solution2
    for num in combinations(nums, 3):
        n=sum(num)
        print(num)

        for i in range(2, n//2+1):
            if n%i==0:
                break
        else:
            answer+=1
            
    return answer

def n_and_m(start, cnt, nums, result):
    global answer
    
    if cnt == 3:
        num=sum(result)
        
        for i in range(2, num//2+1):
            if num%i==0:
                break
        else:
            answer+=1
    else:    
        for i in range(start, len(nums)):
            result[cnt]=nums[i]
            
            n_and_m(i+1, cnt+1, nums, result)

print(solution([1,2,3,4]))
        