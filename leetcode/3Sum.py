
class Solution:
    # n^3 시간초과. n^2도 간당간당 하므로 조건 걸어서 줄여줘야함. 
    # two pointer로 푸는 게 best 
    def threeSum(self, nums):
        if len(nums)<2:
            return []

        m={}
        nums = sorted(nums)

        for num in nums:
            m.setdefault(num, 0)
            m[num]+=1
        
        answer=[]
        # 맨 앞 고정
        for i in range(len(nums)):
            # 맨 앞이 양수이면 무조건 0보다 크므로 종료
            if nums[i]>0:
                break

            # 근접한 애가 중복이면 pass 
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            m[nums[i]]-=1
            # 두번째 고정
            for j in range(i+1, len(nums)):
                m[nums[j]]-=1
                
                target=-(nums[i]+nums[j])
                if target in m and m[target]>0:
                    tmp=sorted([nums[i], nums[j], target])
                    answer.append(tmp)

                m[nums[j]]+=1
            m[nums[i]]+=1

        return list(map(list, set(map(tuple, answer))))
        
if __name__=="__main__":
    sol1 = Solution()
    print(sol1.threeSum([-1,0,1,2,-1,-4]))