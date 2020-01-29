a = "12:00:00.100"

time_a = a.split(":")

time_a = list(map(float, time_a))
print(time_a[0]*3600 + time_a[1]*60 + time_a[2])
