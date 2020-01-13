import re 
    
def solution(files):    
    file_sort=[]
    for file in files:
        head=re.match('[^0-9]+', file)
        number=re.match('[0-9]+', file[head.end():])
        file_sort.append([head.group(), number.group(), file[head.end()+number.end():]])
    
    file_sort=sorted(file_sort, key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(f) for f in file_sort]

# print(solution(['foo9.txt', 'foo010bar020.zip', 'F-15']))
print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))