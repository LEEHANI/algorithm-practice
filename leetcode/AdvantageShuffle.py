class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a = sorted(A)
        b = sorted(B)
        remain = []
        m={}
        answer=[]

        j=0
        # a를 기준으로 루프
        for i in range(len(A)):
            # b[j]에 매핑되는 값을 m에 추가 ex) {0: [1, 2]}
            if a[i] > b[j]:
                m.setdefault(b[j], []).append(a[i])
                j+=1
            # a[i] <= b[j]이면 remain 큐에 추가
            else:
                remain.append(a[i])

        # remain에 남아있는 값은 A[i] > B[i]을 만족하지 못하는 값이므로 b[j:] 하나씩 할당
        for i in range(j, len(A)):
            m.setdefault(b[i], []).append(remain.pop(0))

        for i in range(len(A)):
            # m[B[i]].pop(0) 이든 m[B[i]].pop() 이든 상관없음.... 문제에 그런 조건이 없기 때문
            answer.append(m[B[i]].pop())
        
        return answer

if __name__=="__main__":
    sol1 = Solution()
    print(sol1.advantageCount(([2,0,4,1,2], [1,3,0,0,2])) 