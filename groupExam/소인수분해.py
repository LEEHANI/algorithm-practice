n=int(input())
MAX_N=10000000
i=2
while i<MAX_N+1:
    if n==1:
        break

    if n%i==0:
        n=n//i
        print(i)
    else:
        i+=1