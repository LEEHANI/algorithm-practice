str = input()
happy = str.count(":-)")
sad = str.count(":-(")

if happy == sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif sad > happy:
    print('sad')
else:
    print('unsure')
