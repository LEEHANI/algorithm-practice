class Solution:
    #O(n2)
    def countSubstrings(self, s: str) -> int:
        # 맨 앞, 맨 뒤를 제외한 값이 팰린드롬인지 map에 저장해놓고, 갖다씀
        # 그래서 맨 앞과 맨 뒤의 값이 같고, 사이의 값이 팰린드롬이면 그 값은 팰린드롬임
        # ex) a___a가 팰린드롬? m = { ___ : True or False }
        m={}
        answer=len(s)
        for i in range(2, len(s)+1):
            for j in range(len(s)-i+1):
                if s[j]==s[j+i-1]:
                    # base case
                    if i==2 or i==3:
                        m[(j, j+i-1)]=True
                        answer+=1
                        continue
                    
                    if m[(j+1, j+i-2)]:
                        m[(j, j+i-1)]=True
                        answer+=1
                    else:
                        m[(j, j+i-1)]=False
                else:
                    m[(j, j+i-1)]=False
        return answer