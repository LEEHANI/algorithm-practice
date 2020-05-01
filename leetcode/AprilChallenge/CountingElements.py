arr=[1,1,3,3,5,5,7,7]

MAX=1001
counting_arr=[0]*MAX
answer=0
for a in arr:
    counting_arr[a]+=1

for i in range (MAX-1):
    if counting_arr[i] and counting_arr[i+1]:
        answer+=counting_arr[i]
print(answer)
