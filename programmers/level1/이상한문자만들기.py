def solution(s):
    answer = ''
    index=0
    split_str=0
    while index<len(s):
        
        if s[index] == ' ':
            split_str=0
            answer += ' '
            index +=1
            continue
        
        if split_str%2 == 0:
            answer += s[index].upper()
        elif split_str%2 == 1:
            answer += s[index].lower()
        
        index +=1
        split_str +=1
    return answer
print(solution('try hello   world'))