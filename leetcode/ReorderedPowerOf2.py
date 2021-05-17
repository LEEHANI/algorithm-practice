'''
양수 N이 있을 때, 10진수를 재정렬해서 2의 거듭제곱이 되는지 판단하라. 
원래 주어진 N의 값을 포함하여. including the original order
즉, 16도 2의 거듭제곱이므로 True

2의 거듭제곱인지 판단하려면? 
10진수를 2진수로 바꿨을 때, 첫자리가 1이고 나머지가 0으로 이루어져야함. 
   1(2)  1(10)
  10(2)  2(10)
 100(2)  4(10) 
1000(2)  8(10)

'''
import itertools 

# O(10!*3), O(?)
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        for permutation in itertools.permutations(str(N), len(str(N))):
            tmp = bin(int(''.join(permutation)))[2:]
            if permutation[0] != '0' and tmp.count('1') == 1:
                return True
            
        return False