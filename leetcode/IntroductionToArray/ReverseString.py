s=["H","a","n","n","a","h"]
for i in range(len(s)//2):
    s[i],s[-i-1]=s[-i-1],s[i]
print(s)