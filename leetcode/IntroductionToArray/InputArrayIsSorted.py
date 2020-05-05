numbers=[0,0,1,2]
target=1
result=[]

left,right=-1,len(numbers)-1
s=-10000
while s!=target:
    if s < target:
        left+=1
    else:
        right-=1

    s=numbers[left]+numbers[right]
print([left+1,right+1])