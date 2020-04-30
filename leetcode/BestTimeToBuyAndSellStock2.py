prices=[7,1,5,3,6,4]
answer=0
# stock=prices[0]
# MAX=3*10**4+1
# for i in range(1,len(prices)):
#     if prices[i]<stock:
#         stock=prices[i]
#     else: # prices[i] > stock
#         if i+1<len(prices) and prices[i]<prices[i+1]:
#             continue
#         answer+=prices[i]-stock
#         stock=MAX

# stock을 팔고 바로 살 수 있으므로 위에 코드를 아래로 바꿀 수 있다. 
for i in range(1,len(prices)):
    if prices[i-1]<prices[i]:
        answer+=prices[i]-prices[i-1]
print(answer)