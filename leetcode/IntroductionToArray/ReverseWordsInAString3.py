s="Let's take LeetCode contest"

temp=''
answer=''
for i in range(len(s)):
    if s[i]!=' ':
        temp+=s[i]
    else:
        answer+=''.join(reversed(list(temp)))
        answer+=s[i]
        temp=''
answer+=''.join(reversed(list(temp)))
print(answer)