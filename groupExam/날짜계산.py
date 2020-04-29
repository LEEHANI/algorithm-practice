e,s,m=map(int,input().split())
if e==15:
    e=0
if s==28:
    s=0
if m==19:
    m=0
i=1
while 1:
    if i%15 == e and i%28 == s and i%19 == m:
        break
    i+=1
print(i)