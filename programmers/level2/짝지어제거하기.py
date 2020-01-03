def solution(s):
    
    stack=[]
    
    stack.append(s[0])
    for c in s[1:]:
        if len(stack) and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
            
    if len(stack):
        return 0
    return 1        

print(solution("baabaa"))
print(solution("cdcd"))