s='loveleetcode'


counting=[0]*26
for ss in s:
    counting[ord('a')-ord(ss)]+=1
for i,v in enumerate(s):
    target=counting[ord('a')-ord(v)]
    if target>1:
        continue
    elif target == 1:
        # return i
        print(i)
        break
else:
    # return -1
    print(-1)