import sys
input = sys.stdin.readline

t=int(input())
for n in range(t):
    n=int(input())
    applicant=[0]*(n+1)
    answer=1
    current_high_score=0
    for i in range(n):
        i,j=list(map(int,input().split()))
        applicant[i]=j

    # nlogn 시간초과
    # applicants=sorted(applicants, key=lambda x:x[0])

    current_high_score=applicant[1]
    for i in range(2,n+1,1):
        if applicant[i] < current_high_score:
            answer+=1
            current_high_score=applicant[i]
    print(answer)
