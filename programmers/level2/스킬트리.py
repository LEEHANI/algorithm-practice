def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_index=[27]*len(skill)
        
        for i, s in enumerate(skill):
            try:
                skill_index[i]=list(skill_tree).index(s) # 스킬 사용 순서 담기
            except ValueError as identifier:
                pass
        
        for i in range(len(skill)-1):
            if skill_index[i] <= skill_index[i+1]:
                continue
            else:
                break
        else: # for-else는 중간에 break 등으로 끊기지 않고 끝까지 수행되면 else문이 실행       
            answer+=1        
    return answer

# print(solution("CBD", ['BACDE', 'CBADF', 'AECB', 'BDA']))
print(solution("CBD", ['BACDE', 'AC', 'CBADF']))