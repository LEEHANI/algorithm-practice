def solution(cacheSize, cities):
    answer = 0
    
    cache_hit=1
    cache_miss=5
    cache=[]
    
    if cacheSize == 0:
        return len(cities)*cache_miss
    
    for city in cities:
        city=city.lower()
        
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer+=cache_hit
        else:    
            if len(cache) < cacheSize:
                cache.append(city)
                answer+=cache_miss
            else:
                cache.pop(0)
                cache.append(city)
                answer+=cache_miss
        
        print(cache, city, answer)    
    return answer

# print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
# print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
# print(solution(1, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
# print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'newyork']))
# print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'newyork']))
# print(solution(2, ['Jeju', 'jeju']))