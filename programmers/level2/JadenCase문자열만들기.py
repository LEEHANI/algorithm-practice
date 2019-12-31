def solution(s):
    answer = '' + s[0].upper()
    
    for i in range(1,len(s),1):
        if s[i-1] == ' ' and s[i] != ' ':
            answer += s[i].upper()
            continue
        answer += s[i].lower()
    return answer   
 
print(solution('3people unFollowed me  ab'))
print(solution('for the last week'))
