def find_character(name):
    
    print(len(name)//2)
    for i in range(len(name)//2):
        print(i,name[i],name[-i])
        if name[i] != 'A':
            return i
        if name[-i] != 'A':
            return -i
        
def solution(name):
    if name.count('A') == len(name):
        return 0
    
    answer = -1
    name=list(name)
    c=''
    while len(name):
        if name.count('A') == len(name):
            break
        
        if name[0] != 'A':
            c=name.pop(0)
        elif name[-1] != 'A':
            c=name.pop()
            if answer == -1:
                answer+=1
        else:
            i=find_character(name)
            if i==None:
              c=name.pop()  
            elif i>0:
                for p in range(i):
                    c=name.pop(0)
                answer +=i-1
            else:
                for p in range(abs(i)):
                    c=name.pop()        
                answer += abs(i)-1
            # print(c,i)    
        answer+=1
        
        temp=ord(c)-ord('A')
        print(c, answer, temp)
        if temp > 13:
            temp= abs(temp-26)
        answer+=temp    
        
    return answer

def solution2(name):
    answer = 0
    visited=[0]*len(name)
    cursor=0
    move=0
    print(visited, sum(visited), len(name))
    
    while sum(visited) != len(name):
        
        if not visited[cursor] and name[cursor] != 'A':
            c=name[cursor]
            visited[cursor]=1
        else:
            
            pass
        
        temp=ord(c)-ord('A')
        if temp > 13:
            temp= abs(temp-26)
        answer+=temp    
        
        for i in range(1,len(name),1):
            try:
                if name[cursor+i] != 'A':
                    move=i
                    break
                if name[cursor-i] != 'A':
                    move=-i
                    break
            except IndexError as identifier:
                pass
        print(c, temp, answer, move)
        answer+=move
        cursor+=move    
        # cursor += 1
    return answer

# print(solution2("JEROEN")) #56
print(solution2("JAN")) #23
# print(solution("AZA"))
# print(solution("AZAA"))
# print(solution("A"))
# print(solution("AAAAAAA"))
# print(solution("JAABAN"))
# print(solution("AAAB"))
# print(solution("AZAAAZ"))
# print(solution("AAAZAAZA"))