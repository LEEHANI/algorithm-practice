def solution(phone_book):
    phone_book.sort()
    
    for i,phone in enumerate(phone_book):
        
        for j in phone_book[i+1:]:
            if phone == j[0:len(phone)]:
                return False
        
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))