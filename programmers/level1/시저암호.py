def solution(s, n):
    answer=''
    
    for character in list(s):
        if 'a'<= character <= 'z':
            answer+=chr(((ord(character)-ord('a'))+n)%26+ord('a'))
        elif 'A'<= character <= 'Z':
            answer+=chr(((ord(character)-ord('A'))+n)%26+ord('A'))
        else:
            answer+=character
    return answer
print(solution('AB',1))
print(solution('z',1))
print(solution('a B z',4))