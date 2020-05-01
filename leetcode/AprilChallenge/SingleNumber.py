from typing import List
from _collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic=defaultdict(int)

        for num in nums:
            dic[num]+=1
        
        for num in nums:
            if dic[num] != 2:
                return num

if __name__=="__main__":
    sol1 = Solution()
    List=[2,2,1]
    print(sol1.singleNumber(List))