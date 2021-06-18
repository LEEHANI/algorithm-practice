'''
https://leetcode.com/problems/matchsticks-to-square/

배열을 4개의 동일한 크기로 쪼갤 수 있는지 묻는 문제. 

중요 포인트
1. 그렇다면 한 변의 크기를 몇으로 할건지? 
  - 정사각형이기 때문에 시도해볼 수 있는 크기가 1가지 밖에 없다. => (놓친 포인트)
2. 크기를 정했으면, 어떻게 쪼개볼건지?
  - 배열 사이즈가 15로 정해져있으므로 다 시도해보자 
'''
class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        global answer
        answer=False
        
        # Check square
        if sum(matchsticks)%4 != 0:
            return False

        matchsticks.sort()
        
        self.bfs(sum(matchsticks)//4, 0, 0, 0, matchsticks)
        
        return answer
    
    def bfs(self, stickSize, pick, total, idx, arr):
        global answer
        
        # Find Answer then finish
        if answer:
            return 

        if total == 4:
            # Check Use all the matchsticks
            if arr.count(-1) == len(arr):
                answer = True
            return 
        
        if pick == stickSize:
            self.bfs(stickSize, 0, total+1, 0, arr)
        elif pick > stickSize:
            return; 
        
        for i in range(idx, len(arr)):
            if arr[i]>= 0:
                tmp=arr[i]
                # Use matchstick
                arr[i]=-1
                self.bfs(stickSize, pick+tmp, total, i+1, arr)    

                # Release matchsticks
                arr[i]=tmp
                
                if answer:
                    # return 