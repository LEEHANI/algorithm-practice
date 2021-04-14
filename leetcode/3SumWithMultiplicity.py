class Solution(object):
    def threeSumMulti(self, arr, target):
        global answer
        answer=0
        mzip={}

        for a in arr:
            if a in mzip:
                mzip[a]=mzip[a]+1
            else:
                mzip[a]=1
        self.nAndM(list(mzip), -1, 0, [0,0,0], target, mzip)

        return answer % (10**9+7)


    def nAndM(self, arr, idx, dep, m, target, mzip):
        global answer 

        if dep == 3:
            for i in range(3):
                if m.count(m[i]) > mzip[m[i]]:
                    return
            if sum(m) == target:
                if m[0]!=m[1] and m[1]!=m[2] and m[0]!=m[2]:
                    answer+= mzip[m[0]]*mzip[m[1]]*mzip[m[2]]
                elif m[0]==m[1] and m[1]==m[2] and m[0]==m[2]:
                    answer+=mzip[m[0]]*(mzip[m[0]]-1)*(mzip[m[0]]-2)//6
                elif m[0]==m[1] and m[0]!=m[2] and m[1]!=m[2]:
                    answer+=(mzip[m[0]]*(mzip[m[0]]-1)//2)*mzip[m[2]]
                elif m[1]==m[2] and m[0]!=m[1] and m[0]!=m[2]:
                    answer+=(mzip[m[1]]*(mzip[m[1]]-1)//2)*mzip[m[0]]
            return
        else:
            for i in range(len(arr)):
                if i < idx:
                    continue
                m[dep]=arr[i]
                self.nAndM(arr, i, dep+1, m, target, mzip)    


if __name__=="__main__":
    sol1 = Solution()
    # print(sol1.threeSumMulti([1,1,2,2,2,2],5)) 
    print(sol1.threeSumMulti([1,1,2,2,3,3,4,4,5,5] ,8)) 
            