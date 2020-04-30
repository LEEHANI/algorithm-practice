import sys 
input = sys.stdin.readline
n=int(input())
answer=99

if n<=99:
    answer=n

# 100 101 102 103 104 105 106 
# 99~
# 100이상일때
# 111 123 136 147 159 
# 210 222 234 257 269 
for i in range(100,n+1):
    s=str(i)
    d=int(s[0])-int(s[1])

    for j in range(len(s)-1):
        if int(s[j])-int(s[j+1])!=d:
            break
    else:
        answer+=1

print(answer)
