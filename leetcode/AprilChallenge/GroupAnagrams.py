from collections import defaultdict

strs=["eat", "tea", "tan", "ate", "nat", "bat"]

# dic=defaultdict(str)

dic={}
answer=[]
i=0
for str in strs:
    str_s=''.join(sorted(str))
    
    try:
        idx=dic[str_s]
        answer[idx].append(str)
    except KeyError as identifier:
        dic[str_s]=i
        i+=1
        answer.append([str])

for i in range(len(answer)):
    answer[i].sort()
        
print(answer)

