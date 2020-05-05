strs=['dog','racecar','car']

if len(strs) == 0:
    # return ''
    pass

target=strs[0]
for k,v in enumerate(strs):
    if len(v) < len(target):
        target=v

strs.remove(target)

for s in strs:
    for i in range(len(target)):
        if target[i]==s[i]:
            continue
        else:
            if i == 0:
                target=''
            else:
                target=target[:i]
            break

print(target)