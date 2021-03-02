class Solution:
    # O(n), O(n)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr=[0]*(len(nums)+1)
        
        for n in nums:
            arr[n]=arr[n]+1
            
        missing=0
        duplicate=0
        for i in range(1,len(arr)):
            if arr[i]==0:
                missing=i
            if arr[i]>1:
                duplicate=i
                
        return [duplicate, missing]