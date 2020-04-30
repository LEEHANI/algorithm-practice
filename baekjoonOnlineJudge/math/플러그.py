import sys 
input = sys.stdin.readline
n=int(input())
answer=0
for i in range(n):
    multi_tab=int(input())

    answer+=multi_tab-1
print(answer+1)
