def solution(w,h):
    
    total=int(w*h)
    remove=0
    w,h=min(w,h),max(w,h)
    print(w/2, h/3)
    print(w%2, h%3)
    if w/2==h/3:
        remove=4*(w/2)
    elif w%2==h%3:
        remove=4*(w/2)+w%2
    elif w==h:
        remove=w
        
    return int(total-remove)

print(solution(8,12))