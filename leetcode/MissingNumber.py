class Solution:
    # O(n), O(1)
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        answer = size*(size+1)//2
        
        return answer - sum(nums)