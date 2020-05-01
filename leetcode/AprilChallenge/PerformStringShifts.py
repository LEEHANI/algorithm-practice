s = "xqgwkiqpif"
shift =[[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]


answer=''
left=0
right=0

for shif in shift:
    if shif[0]==0:
        left+=shif[1]
    else:
        right+=shif[1]

result=(left-right)%len(s)

#right로 이동 
if result<0:
    answer+=s[result:]
    answer+=s[:len(s)+result]
# left로 이동 
elif result>0:
    answer+=s[result:]
    answer+=s[:result]
# 그대로 
else:
    answer=s
print(answer)