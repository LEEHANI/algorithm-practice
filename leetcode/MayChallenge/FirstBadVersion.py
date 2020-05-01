# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution:
    def __init__(self):
        self.answer = 0

    def firstBadVersion(self, n):
        self.binarySearch(1,n)
        return self.answer
        
    def binarySearch(self,start,end):
        if start<end:
            mid=(start+end)//2

            result = isBadVersion(mid)

            if result == False:
                binarySearch(mid+1,end)
            else:
                self.answer=mid
                binarySearch(start,mid-1)


        


# 0 5 2 false
# 3 5 4 true 