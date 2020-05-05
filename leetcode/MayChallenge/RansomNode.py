ransomNote='aa'
magazine='ab'

counting=[0]*26
answer=True
for m in magazine:
    counting[ord('a')-ord(m)]+=1
    
for r in ransomNote:
    temp=ord('a')-ord(r)
    if counting[temp]:
        counting[temp]-=1
        continue
    else:
        answer=False
        break

print(answer)