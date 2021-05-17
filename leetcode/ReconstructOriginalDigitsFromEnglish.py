'''
zero one two three four five six seven eight nine 
 z        w          u        x          g         <---- unique
one three five seven nine 
 o    h     f     s
nine 
 i   
'''
class Solution:
    def originalDigits(self, s: str) -> str:
        answer=[]

        filtering = [['z', 0, 'zero'], 
                    ['w', 2, 'two'], 
                    ['u', 4, 'four'], 
                    ['x', 6, 'six'], 
                    ['g', 8, 'eight'], 
                    ['o', 1, 'one'], 
                    ['h', 3, 'three'], 
                    ['f', 5, 'five'], 
                    ['s', 7, 'seven'],
                    ['i', 9, 'nine']]
        
        for i in range(10):    
            tmp = s.count(filtering[i][0])
            if tmp:
                for t in range(tmp):
                    answer.append(filtering[i][1])
                for c in range(len(filtering[i][2])):
                    s=s.replace(filtering[i][2][c], "", tmp)

        answer = sorted(answer)
        return ''.join(str(x) for x in answer)


if __name__=="__main__":
    sol1 = Solution()
    # print(sol1.originalDigits('fviefuro'))
    # print(sol1.originalDigits('owoztneoer'))
    print(sol1.originalDigits('zerozero'))