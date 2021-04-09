class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        phones = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        
        global answer
        answer=[]

        self.dfs(digits, phones, 0, '')

        return answer

    def dfs(self, digits, phones, idx, letters):
        global answer

        if idx == len(digits):
            answer.append(letters)
            return

        target = int(digits[idx])
        for i in range(len(phones[target])):
            self.dfs(digits, phones, idx+1, letters+phones[target][i])

if __name__=="__main__":
    sol1 = Solution()
    print(sol1.letterCombinations(""))