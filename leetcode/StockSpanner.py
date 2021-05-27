'''
문지기를 만나면, 문지기 이전의 값은 쓸모가 없게된다. 문지기라 함은 A > B를 뜻한다 
예를들어, [1,2,5,3,2,4] 일때, 
price=3, [1,2,5,3] 그 전의 값이 5이기 때문에 문지기를 만났다. (A > B). 문지기:5
price=2, [1,2,5,3,2] 그 전의 값이 3이기 A > B 때문에 문지기를 만났다. 문지기:3
price=4, [1,2,5,3,2,4] 그 전의 값이 2,3이고 5에서 A > B 때문에 문지기를 만났다. 문지기:5
현재 price 값이 클수록 문지기 만날 확률이 줄어듦

A <= B 일때는 이 수를 합쳐도된다. 
[8,3,2,4,5,6] 일때, price=6라면 문지기 8을 만나기 전의 값인 [3,2,4,5]이다. 
5를 연속 일수로 셀 수 있으면 그 전의 날인 [3,2,4]도 자연히 따라올 수 밖에 없다. 
따라서 이를 매번 세는것보다 압축해서 나타낼 수 있다. [value, count] ~ [[8,1],[5,4]]
'''
class StockSpanner:

    def __init__(self):
        self.stack=[]       

    def next(self, price: int) -> int:
        if len(self.stack)==0:
            self.stack.append([price, 1])
            return 1
        
        if self.stack[-1][0]>price:
            self.stack.append([price, 1])
            return 1
        else:
            total=1
            value=0
            count=0
            

            while self.stack:
                value, count=self.stack.pop()
                
                if value > price:
                    self.stack.append([value, count])
                    break
                else:
                    total+=count
                    
            self.stack.append([price, total])
            return total
                    
                


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)