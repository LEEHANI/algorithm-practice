stones=[2,7,4,1,8,1]

while 1:
    stones.sort()
    if 2<=len(stones):
        x,y=stones.pop(-1),stones.pop(-1)
        if x==y:
            continue
        else:
            stones.append(abs(x-y))
    else:
        break

print(stones)

if stones:
    print(stones[0])
else:
    print(0)