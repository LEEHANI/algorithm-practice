def solution(n):
    
    answer = n
    s=format(n,'b').count('1')
    
    while True:
        answer +=1
        if s==format(answer,'b').count('1'):
            return answer
    
print(solution(78))