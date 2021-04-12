class Solution:
    # O(n)
    def countBits(self, num: int) -> List[int]:
        answer=[0,1,1,2]

        target=4
        j=0
        
        for i in range(4, num+1):
            if j==target:
                j=0
                target=i
            answer.append(answer[j]+1)
            j+=1
        
        return answer[:num+1]