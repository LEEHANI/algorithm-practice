N=3
trust=[[1,3],[2,3]]


counting=[0]*(N+1)

for p,t in trust:
    counting[p]-=1
    counting[t]+=1

answer=-1
for i in range(1,len(counting)):
    if counting[i]==(N-1):
        answer=i

print(answer)