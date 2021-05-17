class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        global start
        global end
        start=-1
        end=-1
        
        mid = self.BSFirst(0, len(nums)-1, nums, target)
        
        if mid>-1:
            start=10000000
            self.BSLeft(0, mid, nums, target)
            self.BSRight(mid, len(nums)-1, nums, target)
            
            if start==-1:
                start=mid
            if end==-1:
                end=mid
        
        return [start, end]
    
    def BSLeft(self, f, r, nums, target):
        global start
        
        if f > r:
            return -1
        
        mid = (f+r)//2
        if nums[mid]==target:
            start=min(mid,start)
        
        if nums[mid]<target:
            return self.BSLeft(mid+1, r, nums, target)
        elif nums[mid]>=target:
            return self.BSLeft(f, mid-1, nums, target)
            
    def BSRight(self, f, r, nums, target):
        global end
        
        if f > r:
            return -1
        
        mid = (f+r)//2
        
        if nums[mid]==target:
            end=max(mid,end)     
        
        if nums[mid]<=target:
            return self.BSRight(mid+1, r, nums, target)
        elif nums[mid]>target:
            return self.BSRight(f, mid-1, nums, target)
    
    def BSFirst(self, f, r, nums, target):
        if f > r:
            return -1
        
        mid = (f+r)//2
        
        if nums[mid]==target:    
            return mid
        
        if nums[mid]<target:
            return self.BSFirst(mid+1, r, nums, target)
        elif nums[mid]>target:
            return self.BSFirst(f, mid-1, nums, target)
        