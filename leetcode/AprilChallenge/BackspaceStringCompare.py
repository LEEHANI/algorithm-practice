S='a##cC'
T='#a#cC'
S_q,T_q=[],[]

for s in S:
    if s=='#':
        if S_q:
            S_q.pop()
    else:
        S_q.append(s)

for t in T:
    if t=='#':
        if T_q:
            T_q.pop()
    else:
        T_q.append(t)
        
if S_q==T_q:
    print('True')
else:
    print('False')