def solution(n,a,b):
    answer = 0

    while a!=b:
        
        if a%2 == 0:
            a=a//2
        else:
            a=a//2+1
            
        if b%2 == 0:
            b=b//2
        else:
            b=b//2+1
        answer+=1
        
    return answer

print(solution(8,4,7))