FBI = 0
for i in range(5):
    if input().count("FBI") > 0:
        FBI = 1
        print(i+1, end=" ")

if not FBI:
    print("HE GOT AWAY!")
