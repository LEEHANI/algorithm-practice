n=int(input())
nums=list(map(int,input().split()))
dic={}

for num in nums:
    try:
        dic[num]=dic[num]+1
    except KeyError as identifier:
        dic[num]=1

m=int(input())
check=list(map(int,input().split()))

for num in check:
    try:
        print(dic[num],end=' ')
    except KeyError as identifier:
        print(0,end=' ')