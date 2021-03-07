class Solution:
    // O(n), O(n)
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0)>1:
            return True
        
        m = {}
        for a in arr:
            m[a]=a        

        for a in arr:   
            if a!=0 and a%2==0 and a//2 in m:
                return True
            
        return False