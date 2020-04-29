import sys 
input = sys.stdin.readline

n=int(input())
q=[]
arr=[]
answer=[]

for i in range(n):
    arr.append(int(input()))

i,j=1,0
while i<n+1 or j<n:
    if i > n+5:
        answer=['NO']
        break

    target=arr[j]
    if q and q[-1]==target:
        q.pop()
        answer.append('-')
        j+=1
    else:
        q.append(i)
        i+=1
        answer.append('+')

for i in answer:
    print(i)