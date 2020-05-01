nums=[1,2,3,4]
answer=-1
max_num=max(nums)
for num in nums:
    if num==max_num:
        continue
    if num != max_num and num*2<=max_num:
        continue
    break
else:
    answer=nums.index(max_num)
print(answer)
