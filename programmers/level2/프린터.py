def solution(priorities, location):
    answer = 0
    
    priorities=list(zip(priorities, list(range(0,len(priorities)))))
    priority=max(priorities)
    
    while 1:
        v,i=priorities.pop(0)

        if v==priority[0]:
            answer+=1
            
            if i==location:
                return answer
            
            priority=max(priorities)
            continue
        priorities.append((v,i))
        
        # print(priorities, priority, location)

# print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))