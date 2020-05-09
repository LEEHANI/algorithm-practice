s=11
nums=[1,2,3,4,5]
# 3 6 10  9 14 



answer=len(nums)+1
temp=0
pointer=0

for i,v in enumerate(nums):

    temp+=v
    while s <= temp:
        answer=min(answer,i-pointer+1)
        temp-=nums[pointer]
        pointer+=1

print(answer, temp)