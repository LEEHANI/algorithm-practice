
nums=[1,0]


temp=0
count=0
answer=0
for num in nums:

    if temp==num:
        count+=1
    else:
        if count==1:
            answer=temp
        temp=num
        count=1
print(answer)