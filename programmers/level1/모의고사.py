def solution(answers):
    answer = []
    supo1=[1,2,3,4,5]
    supo2=[2,1,2,3,2,4,2,5]
    supo3=[3,3,1,1,2,2,4,4,5,5]
    supo1_count, supo2_count, supo3_count =0,0,0
    
    for i,v in enumerate(answers):
        if v == supo1[i%len(supo1)]:
            supo1_count +=1
        if v == supo2[i%len(supo2)]:
            supo2_count +=1
        if v == supo3[i%len(supo3)]:
            supo3_count +=1
    
    supo_max = max(supo1_count, supo2_count, supo3_count)
    # print(supo_max, supo1_count, supo2_count, supo3_count)            
    
    if supo_max == supo1_count:
        answer.append(1)
    if supo_max == supo2_count:
        answer.append(2)
    if supo_max == supo3_count:
        answer.append(3)        
    
    return answer
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))