nums=[1,1,2]

point1=0
for point2 in range(1,len(nums)):
    if nums[point1]!=nums[point2]:
        point1+=1
        nums[point1]=nums[point2]

print(point1)