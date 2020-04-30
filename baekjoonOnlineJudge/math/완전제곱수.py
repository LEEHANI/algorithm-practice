import math

m=int(input())
n=int(input())
answer=[]
for i in range(m,n+1):
    if int(math.sqrt(i))**2==i:
        answer.append(i)
if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)

    