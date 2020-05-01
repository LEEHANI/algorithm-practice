nums=[-1,-1,0,1,1,0]

left=0
right=sum(nums[1:])
for i in range(len(nums)):
    if left==right:
        print(i)
        break
    left+=nums[i]
    if i+1<len(nums):
        right-=nums[i+1]
    
else:
    print(i)