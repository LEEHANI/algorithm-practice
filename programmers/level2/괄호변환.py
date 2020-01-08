def solution(p):
    p=list(p)
    if len(p) == 0:
        return ""
    
    l,r=0,0
    u=p.pop(0)
    
    correct_flag=1
    if u == "(":
        l=1
    else:
        correct_flag=0
        r=1   
        
    while l!=r:
        u+=p.pop(0)
    
        if u[-1] == "(":
            l+=1
        else:
            r+=1  
    v=p        
    if correct_flag:
        return u+solution(v)
    else:
        new_u=""
        for i in u[1:-1]:
            if i=="(":
                new_u+=")"
            else:
                new_u+="("    
        return "("+solution(v)+")"+new_u
    
# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))