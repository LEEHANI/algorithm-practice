rowIndex=7

arr=[1]*(rowIndex+1)
for k in range(2,rowIndex+1):
    for i in range(k-1,0,-1):
        arr[i]=arr[i]+arr[i-1]
print(arr)