candies=[2,3,5,1,3]
extraCandies=3


answer=[]
greatestCandy=max(candies)
for i,v in enumerate(candies):
    if greatestCandy<=v+extraCandies:
        answer.append(True)
    else:
        answer.append(False)
    
print(answer)