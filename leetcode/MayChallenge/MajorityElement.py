from collections import defaultdict 

nums=[3,3,4]


dic=defaultdict(int)
answer=0

for n in nums:
    dic[n]+=1

    if dic[answer] < dic[n]:
        answer=n
        
print(answer)