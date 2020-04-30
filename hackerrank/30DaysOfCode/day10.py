n=int(input())

binary=[]
while 1:
    if n<=1:
        binary.append(n)
        break

    binary.append(n%2)
    n=n//2
answer=0
count=0
for i in range(len(binary)):
    if binary[i]==1:
        count+=1
    else:
        answer=max(answer,count)
        count=0
print(max(answer,count))
