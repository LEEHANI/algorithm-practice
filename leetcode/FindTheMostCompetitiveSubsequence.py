import heapq

'''
nums = [2,4,3,3,5,4,9,6], k = 4일때, 
[2,4,3,3,5][4,9,6] nums를 k-1으로 나눈다. [2,4,3,3,5] 사이에 min값을 찾으면 된다. 
뒷배열은 k개를 만들기 위해 안전빵으로 남겨놓는다. 이를 반복 한다 

[2,4,3,3,5][4,9,6] k=3, pick=2
[4,3,3,5,4][9,6] k=2, pick=3
[3,5,4,9][6] k=1, pick=3
[5,4,9,6] pick=4

예를들어 [4, 7, 2, 1, 7], k=3 일때, 
뒷배열을 남겨두지 않고 min값을 찾는다면 [7]만 남게되므로 k길이만큼 배열을 채울수가 없다

시간초과?
첫번째 배열에서 min값을 찾을 때, min함수로 찾으면 시간초과가 난다 

'''
class Solution(object):
    def mostCompetitive(self, nums, k):
        answer=[]
        heap=[]
        start=-1

        for i in range(len(nums)-(k-1)):
            heapq.heappush(heap, [nums[i], i])
        
        for i in range(k-1):
            val, start=self.pickOne(start, heap)
            answer.append(val)
            heapq.heappush(heap, [nums[len(nums)-(k-1)+i], len(nums)-(k-1)+i])
        
        # 마지막 값
        answer.append(self.pickOne(start, heap)[0])
        return answer
    
    def pickOne(self, start, heap):
        while heap:
            val, idx=heapq.heappop(heap)
            
            if start<idx:
                return [val, idx]
        