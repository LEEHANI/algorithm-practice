def solution(arrangement):
    answer = 0
    stack=[]

    for i in range(len(arrangement)):
        if arrangement[i]=='(':
            stack.append('(')
        elif arrangement[i]==')':
            stack.pop()
            if i>0 and arrangement[i-1] == ')':
                answer+=1
            else:
                answer+=len(stack)

    return answer

print(solution("()(((()())(())()))(())"))