digits=[4,3,2,1]


carry=0
digits[-1]+=1
for i in range(len(digits)-1,-1,-1):
    if 10<=digits[i]+carry:
        digits[i]=(digits[i]+carry)%10
        carry=1
    else:
        digits[i]=(digits[i]+carry)%10
        carry=0

if carry:
    digits.insert(0,1)

print(digits, carry)