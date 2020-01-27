from itertools import permutations

def solution(baseball):
    answer = 0
    
    arr=[i for i in permutations([1,2,3,4,5,6,7,8,9], 3)]
    
    for a in arr:
        all_cases_pass=1
        for n,s,b in baseball:
            
            strike,ball=0,0
            n=list(map(int,str(n)))
            a=list(a)
            
            for i in range(3):
                if a[i]==n[i]:
                    strike+=1
                elif n.count(a[i]):
                    ball+=1
                    
            if strike!=s or ball!=b:
                all_cases_pass=0
        
        # a가 baseball의 모든 케이스를 다 통과하면
        if all_cases_pass:        
            answer+=1 
            
    return answer

print(solution([[123,1,1],[356,1,0],[327,2,0],[489,0,1]]))