def solution(s):
    if s[-1] == '(':
        return False
    
    s=list(s)
    s.pop()
    count=1
    
    while len(s):
        if s.pop() == "(":
            count-=1            
        else:
            count+=1
        if count<0:
            return False
        
    return False if count else True    
# print(solution("()()"))
# print(solution("(())()"))
# print(solution(")()("))
# print(solution("(()("))
# print(solution("())"))