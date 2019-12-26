def solution(d, budget):
    select=[]
    d.sort()
    
    for i in d:
        select.append(i)
        
        if sum(select) == budget:
            break
        if sum(select) > budget:
            select.pop()     
    return len(select)

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))