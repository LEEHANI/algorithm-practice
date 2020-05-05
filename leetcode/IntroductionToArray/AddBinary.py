a='11'
b='1'

# print(bin(int(a,2)+int(b,2))[2:])

if len(b)>len(a):
    a,b=b,a

b='0'*(len(a)-len(b))+b

result=[]

for i in range(len(a)):
    result.append(int(a[i])+int(b[i]))

carry=0
for i in range(len(result)-1,-1,-1):
    if carry:
        result[i]+=1
        carry=0
    if result[i]>1:
        result[i]=result[i]%2
        carry=1
        
if carry:
    result.insert(0,1)
print(result)