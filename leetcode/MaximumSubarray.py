from typing import List

class Solution:
    def __init__(self):
        self.answer = -1000000000000 

    def maxSubArray(self, nums: List[int]) -> int:
        self.answer=max(nums)

        for i in range(len(nums)):
            if nums[i]>0:
                self.divideAndConquer(i,len(nums), nums)
        return self.answer

    def divideAndConquer(self, start: int, end: int, nums: List[int]):
        if start < end:
            mid=(start+end)//2

            self.divideAndConquer(start, mid, nums)
            self.divideAndConquer(mid+1, end, nums)

            self.answer=max(self.answer, sum(nums[start:end+1]))

if __name__=="__main__":
    sol1 = Solution()
    # List=[-2,-1]
    List=[1,2,-1,-2,2,1,-2,1,4,-5,4]
    #     0 1  2  3  4 5 6
    # List=[-2,1,-3,4,-1,2,1]
    print(sol1.maxSubArray(List))