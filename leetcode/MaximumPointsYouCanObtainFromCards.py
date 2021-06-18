'''
sliding window 
'''
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        total=sum(cardPoints)
        n=len(cardPoints)
        window=sum(cardPoints[:n-k])
        answer=window
        
        for i in range(1, k+1):
            window=window-cardPoints[i-1]+cardPoints[i+n-k-1]
            answer=min(answer,window)
            
        return total-answer