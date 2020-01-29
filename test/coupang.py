def solution(n, min_position, max_position, positions):
    answer=[]
    
    positions.sort()
    
    distance=(max_position-min_position)//(n-1)
    j=0
    for i in range(min_position, max_position+1, distance):
        
        try:
            if i < positions[j]:
                answer.append(i)    
            elif i == positions[j]:
                j+=1
                continue
        except IndexError as identifier:
            answer.append(i)   
             
    return answer

def solution2(n, min_position, max_position, positions):
    interval = (max_position-min_position)//(n-1)
    return [home for home in range(min_position, max_position+1, interval) if home not in positions]
    
print(solution(5,-5,3,[-1,-3,3]))
print(solution2(5,-5,3,[-1,-3,3]))

print(solution(6,-10,10,[6,-10,2,-6]))
print(solution2(6,-10,10,[6,-10,2,-6]))
