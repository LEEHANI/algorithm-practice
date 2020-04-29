
x=int(input())
dp=[0]
idx=0
for i in range(1,x+3,1):
    dp.append(i+dp[i-1])
    if dp[i-1]<x<=dp[i]:
        idx=i
        break
if idx%2==0:
    m,n=idx,1
else:
    m,n=1,idx

count=dp[-1]
for i in range(idx):
    if count==x:
        print(str(m)+'/'+str(n))
        break   
    if idx%2==0:
        m-=1
        n+=1
    else:
        m+=1
        n-=1
    count-=1