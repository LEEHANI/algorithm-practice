nums=[1,0]

count=0
zero_index=-1

for i in range(len(nums)): 
    target=nums[i]

    if target==0:
        count+=1
        if zero_index == -1:
            zero_index=i
    elif zero_index == -1:
        continue
    else:
        nums[zero_index]=target
        zero_index+=1

for i in range(1,count+1):
    nums[-i]=0
