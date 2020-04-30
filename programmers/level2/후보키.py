from itertools import combinations

def solution(relation):
    answer = 0
    columns=[]
    candidate_keys=[]

    # convert row to col
    columns = list(map(list, zip(*relation)))
    for i in range(len(columns)):
        columns[i].append(i)
    row_size=len(columns[0])

    # find single candidate key
    i=len(columns)-1
    while i>-1:
        if row_size == len(set(columns[i])):
            columns.pop(i)        
            answer += 1
        i-=1

    for i in range(2,len(columns)+1,1):
        for combination_columns in combinations(columns,i):
            temp_columns=[]
            for y in range(row_size-1):
                temp_str=''
                for x in range(len(combination_columns)):
                    temp_str+=combination_columns[x][y]
                temp_columns.append(temp_str)
            # print(temp_columns)

            if row_size-1 == len(set(temp_columns)):
                # candidate_keys.append([combination_columns[j][-1] for j in range(len(combination_columns))])
                temp = ''
                for j in range(len(combination_columns)):
                    temp += str(combination_columns[j][-1])
                candidate_keys.append(temp)

    answer_keys = []
    for candidate_key in candidate_keys:    #[02, 03, 13, 34, 134]  --> 134
        is_key = True
        for answer_key in answer_keys:  # [02, 03, 13, 34]
            if not is_key:
                break
            for col in answer_key:      # 02 각각의 값 0, 2가 13에 포함되어있는가?
                #키일 수도 있는 경우
                if col not in candidate_key:
                    break
            else:
                #키가 아닌경우
                is_key=False
                break
            
        if is_key:
            answer_keys.append(candidate_key)

    print(answer_keys)
    return answer+len(answer_keys)

# print(solution([["100", "ryan", "music", "2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# print(solution([
#     ["100","100", "100"], 
#     ["100","200", "300"], 
#     ["200","300", "100"],
#     ["300","200", "200"]]))

print(solution([
    ["b","2","a","a","b"],
    ["b","2","7","1","b"],
    ["1","0","a","a","8"],
    ["7","5","a","a","9"],
    ["3","0","a","f","9"]]))