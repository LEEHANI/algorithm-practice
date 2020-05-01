class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        s=n
        arr=[0]*10
        while 1:         
            for i in str(s):
                sum+=int(i)**2
            s=sum
            sum=0

            if s==1:
                return True
            
            # 무한루프 막기 
            if s<10:
                if arr[s] == 0:
                    arr[s]=1
                else:
                    return False

if __name__=="__main__":
    sol1 = Solution()
    print(sol1.isHappy(4)) 