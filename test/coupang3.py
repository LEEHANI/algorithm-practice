import datetime

def rr(numServer, logs):
    server=[0]*numServer
    
    start=logs[0]
    end=logs[-1]
    

def solution(numServer, logs):
    answer=[]
    
    return answer

# print(int(datetime.datetime.("12:00:00.100 0.400").timestamp))
print(datetime.datetime.strptime("12:00:00.100", "%H:%M:%S.%f").timetuple())
print(datetime.datetime.strptime("12:00:00.100", "%H:%M:%S.%f").toordinal())
print(datetime.datetime.strptime("12:00:00.200", "%H:%M:%S.%f").timestamp())
# print((datetime.datetime.strptime("12:00:00.100", "%H:%M:%S.%f").timestamp))
ts='12:00:00.100'
# print(datetime.datetime.fromtimestamp(int(ts)).strftime('%H:%M:%S'))
# print(sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(ts.split(":")))))
# print(ts.time)