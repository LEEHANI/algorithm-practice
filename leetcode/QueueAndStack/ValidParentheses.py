s=']'


stack=[]
answer=True
open=['{','[','(']
close=['}',']',')']
for i in s:
    if i in open:
        stack.append(i)
    else:
        if stack:
            temp=stack.pop()
            idx=open.index(temp)
            if close[idx]!=i:
                answer=False
                break
        else:
            answer=False
            break


if stack:
    answer=False

print(answer)