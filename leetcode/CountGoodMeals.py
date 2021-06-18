import math
class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        answer=0
        m={}
        powerOfTwo=[]
        deliciousness.sort()
        for n in deliciousness:
            if n in m:
                m[n]+=1
            else:
                m[n]=1
        
        for i in range(23):
            powerOfTwo.append(2**i)

        aleadyCheck=-1
        
        for n in deliciousness:
            # n 근처의 2의 거듭제곱 찾기
            for i in range(20):
                # n과 거듭제곱이 같다면. 4==4
                if n==powerOfTwo[i]:
                    # 0이 있으면 (4, 0)으로 자기 자신 가능 
                    if 0 in m:
                        answer+=m[0]

                    target = powerOfTwo[i+1]-n
                    
                    if n==target and aleadyCheck!=n and target in m:
                        aleadyCheck=n
                        #팩토리얼 더하기 
                        for j in range(m[target]-1, 0, -1):
                            answer+=j

                if powerOfTwo[i-1]<n<=powerOfTwo[i]:
                    target = powerOfTwo[i]-n
                    if target in m:
                        answer+=m[target]
                        break
                    

            answer% (10**9 + 7)

        return answer% (10**9 + 7)
if __name__=="__main__":
    sol1 = Solution()
    # print(sol1.countPairs([1,3,5,7,9]))
    # print(sol1.countPairs([4,4,4,4]))
    # print(sol1.countPairs([2,2,2,6,6,6]))
    print(sol1.countPairs([149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]))