nums=[1,1,0,1,1,1]


nums.append(0)
answer=0
temp=0

for i,k in enumerate(nums):
    if k:
        temp+=1
    else:
        answer=max(temp,answer)
        temp=0

print(answer)