class Solution:
    # Global inversion: i < j, A[i] > A[j]
    # local inversion:         A[i] > A[i+1]
    # 잘 보면 Global안에 local이 들어있다. 
    # 그래서 A[i] > A[i+2....j] 까지 탐색해보고.. 그 값이 존재하면 False 이다. 
    # 하지만 단순하게 찾으면 시간초과 남. 
    # dp를 사용해서 풀었다. 만약, A[i] > A[i+2...j] 인게 존재할까? 이걸 매번 탐색해야할까...
    # A[2, ... ,N-1] 를 탐색해서 가장 낮은 값만 dp에 저장하자. 그래야 A[i] > A[i+2...j]인걸 찾을 수 있으니까
    # A =  [5,4,2,0,1,3]
    # dp = [0,0,0,0,1,3]
    # O(n)
    def isIdealPermutation(self, A):
        # 시간 초과 O(n2)
        # globalInversions = 0 
        # for i in range(len(A)-1):
        #     for j in range(i+2, len(A)):
        #         if A[i] > A[j]:
        #             globalInversions+=1

        # return globalInversions == 0

        dp = [0]*len(A)
        dp[-1] = A[-1]
        # 뒤부터 탐색해서 가장 낮은값 저장하기
        for i in range(-2, -len(A), -1):
            dp[i] = min(A[i], dp[i+1])

        for i in range(len(A)-2):
            if A[i] > dp[i+2]:
                return False

        return True



if __name__=="__main__":
    sol1 = Solution()
    # print(sol1.isIdealPermutation([1,0,2]))
    print(sol1.isIdealPermutation([5,4,1,9,7,3,2]))
    # print(sol1.isIdealPermutation([1,2,0]))
    # 