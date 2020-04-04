from itertools import combinations

def solution(relation):
    answer = 0
    
    col=[]
    # convert row to col
    for i in range(len(relation[0])):
        col.append([relation[j][i] for j in range(len(relation))])
    
    size=len(col[i])
    i=0
    # find single candidate key
    while i<len(col):
        if size == len(list(set(col[i]))):
            col.pop(i)        
            answer += 1
        i+=1
    
    
    i=2
    for one,two in combinations(col,2):
        one=list(one)
        two=list(two)
        
        # print(list(one), list(two))
        temp=[]
        for i in range(size):
            temp.append(one[i]+two[i])
        print(temp)
    # print(list(combinations(col,2)))
    
    return answer

print(solution([["100", "ryan", "music", "2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))