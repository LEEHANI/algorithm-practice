def solution(bridge_length, weight, truck_weights):
    time = 1
    current_weight=0
    pass_bridge=[]
    bridge=[]
    
    while 1:
        time+=1
        
        for b in bridge:
            if bridge_length==time-b[1]:
                pass_bridge.append(bridge.pop(0)[0])
                current_weight-=pass_bridge[-1]
                continue
            break
        
        if len(truck_weights) != 0 and (current_weight + truck_weights[0] ) <= weight:
            bridge.append([truck_weights.pop(0),time])
            current_weight+=bridge[-1][0]
            
        if current_weight==0:
            break
            
        # print(time, pass_bridge, bridge, current_weight, truck_weights)
    return time-1

# print(solution(2,10,[7,4,5,6]))
# print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))