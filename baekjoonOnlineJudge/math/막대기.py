x=int(input())
arr=[64]

while 1:
    if x==sum(arr):
        break

    if x<sum(arr):
        n=arr.pop(-1)//2
        if x<=sum(arr)+n:
            arr.append(n)
        else:
            arr.append(n)
            arr.append(n)
print(len(arr))