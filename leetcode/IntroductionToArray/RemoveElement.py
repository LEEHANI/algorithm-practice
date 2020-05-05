nums=[3,2,2,3]
val=3


j=0
for i in range(len(nums)):
    if nums[i] != val:
        nums[j]=nums[i]
        j+=1


print(j, nums,nums[:j])