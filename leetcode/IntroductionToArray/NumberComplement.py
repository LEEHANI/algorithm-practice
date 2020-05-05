num=8

nNum=''
for n in bin(num)[2:]:
    if n=='0':
        nNum+='1'
    else:
        nNum+='0'
print(int(nNum,2))
nNum=str(int(nNum))
# answer=int(nNum[-1])
# for i in range(len(nNum)-1):
    # if int(nNum[i]):
        # answer+=pow(2,len(nNum)-1-i)

# print(answer)