class Solution:
    def wordSubsets(self, A, B):
        bs = []
        answer=[]
        
        # B를 갖고 카운팅..
        # 카운팅 결과 bs에는 다음과 같이 들어가있음 
        # B=["ec", "oc", "ceo"]
        # bs= [[...1...1....], [....1..1.], [...1..1..1..]]
        for alphabets in B:
            b = [0]*26
            for alpha in alphabets:
                b[ord(alpha)-ord('a')]+=1
            bs.append(b)
        
        resultb=[0]*26
        # A가 B를 다 만족시키려면 B를 다 포괄해야함. 그러므로, bs의 최대 갯수를 가져야함.
        # B=["ec", "oc", "ceo"]
        #    [e, o, c]
        # ec [1, 0, 1]
        # oc [0, 1, 1]
        # ceo[1, 1, 1] 
        #    [1, 1, 1] ===> 애만 만족하면됌
        for i in range(26):
            for j in range(len(B)):
                resultb[i]=max(bs[j][i], resultb[i])
        
        for alphabets in A:
            a = [0]*26

            for alpha in alphabets:
                a[ord(alpha)-ord('a')  ]+=1

            for i in range(26):
                if resultb[i] and resultb[i]>a[i]:
                    break
                
            else:
                answer.append(alphabets)

        return answer

if __name__=="__main__":
    sol1 = Solution()
    print(sol1.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"]))
    # print(sol1.wordSubsets(["acaac","cccbb","aacbb","caacc","bcbbb"], ["c","cc","b"]))
        