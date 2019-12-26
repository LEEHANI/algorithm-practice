def solution(dartResult):
    darts=[]
    point=[0,0,0]
    start=0
    for i,dart in enumerate(dartResult[1:]):
        try:
            if dart in ['S','D','T','#','*'] and 0<=int(dartResult[i+2])<=10:
                darts.append(dartResult[start:i+2])
                start=i+2
        except Exception as identifier:
            pass
    darts.append(dartResult[start:])    
    
    for i,dart in enumerate(darts):
        point[i]=int(dart[0])
        if dart[1] == '0':
            point[i]=10
            dart=dart[1:]
            
        if dart[1] == 'D':
            point[i]=point[i]**2
        elif dart[1] == 'T':    
            point[i]=point[i]**3
            
        if len(dart) >=3:
            if dart[2] == '#':
                point[i] = -point[i]
            elif dart[2] == '*':
                point[i] = point[i]*2
                
                if i>0:
                    point[i-1] = point[i-1]*2
                
    # print(darts, point)        
    return sum(point)
print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))