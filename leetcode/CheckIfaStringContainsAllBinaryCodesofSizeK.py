# O(n), O(?)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        target=0
        m={}
        
        for i in range(k):
            target+=2**i    
        
        for i in range(target+1):
            tmp=bin(i)[2:].zfill(k)
            m[tmp]=False


        for i in range(len(s)-k+1):
            if s[i:i+k] in m:
                m[s[i:i+k]]=True

        for i in m:
            if m[i] == False:
                return False
        
        return True
