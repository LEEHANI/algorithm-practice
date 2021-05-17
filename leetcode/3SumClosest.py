
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        answer =  float('inf')
        
        for i in range(len(nums)):
            target1 = nums[i]

            target2=i+1
            target3=len(nums)-1

            while target2<target3:
                tmp = target1+nums[target2]+nums[target3]

                if tmp == target:
                    return target

                if abs(target - tmp) < abs(target-answer):
                    answer = tmp 

                if tmp < target:
                    target2+=1
                else:
                    target3-=1
                
                # print(target1, nums[target2], nums[target3], tmp, target, answer)
        
        return answer 

if __name__=="__main__":
    sol1 = Solution()
    print(sol1.threeSumClosest([-1,2,1,-4], 1)) # 2 
    # print(sol1.threeSumClosest([0, 0, 0], 1))  # 0 
    # print(sol1.threeSumClosest([1, 1, 1, 0], -100)) # 2