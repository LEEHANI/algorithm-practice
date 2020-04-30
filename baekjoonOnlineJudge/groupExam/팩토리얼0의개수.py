# 0의 갯수를 찾는건 10의 갯수를 찾는 것과 같다..! 
# 10의 갯수를 찾는건 (10), (2,5)의 갯수를 찾는 것과 같다

n=int(input())
answer=0

for i in range(n,0,-1):
    s=str(i)
    temp=i
    
    while 1:
        if temp%10 == 0:
            answer+=1
        else:
            break
        temp=temp/10

    while 1:
        if temp%5 == 0:
            answer+=1
        else:
            break
        temp=temp/5

print(answer)




