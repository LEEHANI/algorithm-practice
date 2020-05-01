# from typing import List

# class Solution:
#     def __init__(self):
#         self.answer = -1000000000000 

#     def maxSubArray(self, nums: List[int]) -> int:
#         self.answer=max(nums)

#         for i in range(len(nums)):
#             if nums[i]>0:
#                 self.divideAndConquer(i,len(nums), nums)
#         return self.answer

#     def divideAndConquer(self, start: int, end: int, nums: List[int]):
#         if start < end:
#             mid=(start+end)//2

#             self.divideAndConquer(start, mid, nums)
#             self.divideAndConquer(mid+1, end, nums)

#             self.answer=max(self.answer, sum(nums[start:end+1]))

# if __name__=="__main__":
#     sol1 = Solution()
#     # List=[-2,-1]
#     List=[1,2,-1,-2,2,1,-2,1,4,-5,4]
#     #     0 1  2  3  4 5 6
#     # List=[-2,1,-3,4,-1,2,1]
#     print(sol1.maxSubArray(List))

# nums=[-2,1]
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# nums=[-2,-1]

# answer=nums[0]
# size=len(nums)
# arr=[]

# target=nums[0]
# for i in range(1,size):
#     if nums[i]<0 and target<0:
#         target+=nums[i]
#     elif nums[i]>0 and target>0:
#         target+=nums[i]
#     else:
#         arr.append(target)
#         target=nums[i]
# arr.append(target)
# print(arr)


# for i in range(size):
#     temp_sum=nums[i]

#     print(answer, temp_sum)
#     if answer < temp_sum:
#         answer=temp_sum

#     for j in range(i+1,size):
#         temp_sum+=nums[j]
#         if answer < temp_sum:
#             answer=temp_sum
# print(answer)


nums=[-2,-5, 1, 4,-1,2,1,-5,4]

dp=[0]*len(nums)
dp[0]=nums[0]
answer=nums[0]
for i in range(1,len(nums)):
    # print(dp, dp[i-1]+nums[i], nums[i], max(dp[i-1]+nums[i],nums[i]))
    dp[i]=max(dp[i-1]+nums[i],nums[i])
    answer=max(answer,dp[i])
print(answer)