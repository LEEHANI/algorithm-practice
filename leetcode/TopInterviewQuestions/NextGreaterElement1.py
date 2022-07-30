'''
O(N^2)는 쉬움

O(N)로 풀고싶으면 stack, map 기술이 필요함 
stack에는 큰 값들을 찾아서 저장
예를들어 [1, 4, 3, 2, 7]이면 [4, 7]을 저장. 

중요한 포인트는 뒤에서부터 진행해야하고, for문이 돌때마다 num의 next greater element값을 저장해두기. 
'''
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []
        
        for num in nums2[::-1]:
            print(num, stack, dic)
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                dic[num] = stack[-1]
            stack.append(num)
            
        return [dic.get(num, -1) for num in nums1]


if __name__=="__main__":
    sol1 = Solution()
    # print(sol1.nextGreaterElement([4,1,2], [1,3,4,2]))
    # print(sol1.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
    print(sol1.nextGreaterElement([4,5,1,2,9], [1,2,5,7,4,3,9]))