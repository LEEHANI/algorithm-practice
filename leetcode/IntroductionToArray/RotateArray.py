import math

nums=[-1,-100,3,99]
k=2


size=len(nums)
g=math.gcd(size,k)
if g==1:
    temp=nums[0]
    target=0
    for i in range(size):
        target=(target+k)%size
        nums[target],temp=temp,nums[target]
else:
    for i in range(g):
        temp=nums[i]
        target=i
        for j in range(0,size//g):
            target=(target+k)%size
            nums[target],temp=temp,nums[target]
            
print(nums)
