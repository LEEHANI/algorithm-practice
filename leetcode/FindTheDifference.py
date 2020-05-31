import collections

s='aabbb'
t='aabbbc'

dic=collections.defaultdict(int)
for i in s:
    dic[i]+=1

answer=''

for i in t:
    if dic[i]==0:
        answer=i
        break
    dic[i]-=1

print(answer)