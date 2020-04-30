n=int(input())
temp=n
answer=0
five=temp//5
temp=temp%5
three=temp//3
temp=temp%3
answer=three+five
while temp!=0:

    five-=1
    temp=5+3*three+temp
    three=temp//3
    temp=temp%3
    answer=three+five
    
    if five < 0:
        answer=-1
        break

print(answer)