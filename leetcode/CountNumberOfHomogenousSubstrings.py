'''
O(n), O(3)
예를들어 "ccccc"가 있을 때 Homogenous Substring은 몇일까?
c, c, c, c, c   5개
cc, cc, cc, cc  4개
ccc, ccc, ccc   3개
cccc, cccc      2개
ccccc           1개
아래로 갈수록 묶음이 커지므로 끝자리만 잘 세면 된다. 그리고 하나씩 숫자가 줄어드는게 보일것이다. 
그럼 n일때는?? 일반화를 해보자
'''
class Solution(object):
    def countHomogenous(self, s):
        target=s[0]
        targetCount=1
        answer=0
        for i in range(1, len(s)):
            if target==s[i]:
                targetCount+=1
            else:
                answer+=(targetCount*(targetCount+1))//2
                answer=answer%(10**9+7)
                target=s[i]
                targetCount=1
            
        if len(target)>0:
            answer+=(targetCount*(targetCount+1))//2
            
        return answer%(10**9+7)