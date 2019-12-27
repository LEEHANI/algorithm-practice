def solution(N, stages):
    answer = []
    stages.sort()
    
    for i in range(N):
        stage_number=i+1
        
        stage_count=(stages.count(stage_number))
        try:
            answer.append([stage_number,stage_count/len(stages)])        
        except ZeroDivisionError as identifier:
             answer.append([stage_number,0])
        stages=stages[stage_count:]
        
    answer=list(reversed(sorted(answer, key=lambda x: (x[1], -x[0]))))
    return [i[0] for i in answer]



# print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4,[4,4,4,4,4]))
print(solution(2,[1,1]))
# print(list(reversed(sorted([1/8,3/7,2/4,1/2,0/1]))))