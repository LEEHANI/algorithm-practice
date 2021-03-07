## 문제풀기
- 시간 초과가 난다면 stack을 써볼까? 

# Python 자료구조 
- arr
  + arr = [0]*10
  + arr = [[0 for col in range(4)] for row in range(5)]
- map
  + m = {}
  + m['abc'] = 123 (삽입)
  + b = m['abc'] (추출)
    - 키값이 없는데 추출하려하면 KeyError 발생한다. in으로 존재 여부 검사해야함 
      ```
      if n in m:
        m[n] += 1
      else:
        m[n] = 1
      ```

# Python 중요 내장 함수 
- `str(5)` # int to str
- 문자열 곱셈 `str += '*'*5` # *****
- `reversed('abcd')` # dcba  
- `list`
  + `list('1234')` # str to list
  + `min([5, 2, 10, 1])` # 1
  + `sum([1, 2, 3, 4])` # 10
  +  `arr.index(value)` # search the list for value
  + 리스트의 덧셈`[1,2,3] + [4,5] = [1,2,3,4,5]`
  + `''.join(['1','2','3','4'])` # list to str
  + 리스트 중복 제거 `arr=list(set(arr))`
  + map(function, iterable)  
    - `list(map(int, arr))` # int(all items of arr)`
  + 정렬
    + `sorted(arr, reverse=True)` # return arr 
      * 정렬 조건 `arr=sorted(arr, key=lambda x: (x[1], -x[0]), reverse=True)`
    + `arr.sort()` # return void
- ascii
  + `ord()` #chr to ascii
  + `chr()` #ascii to chr
- 3항연산 `True if a == 2 else False`

## python slicing 
- `s[start:end:step]`
  + `s[::-1]` 뒤에서부터 출력 # elppa

## python for
- `result = [ r for i in range(10) ]` 
  + `for i in range(10):`
            `result.append(i)`
- `array_2d = [[0 for col in range(5)] for row in range(10)]` # 10*5 배열 생성
- `for-else` for문이 중간에 끊기지 않으면(break를 만나지 않으면) else문이 실행
```python
for i in arr:
  if i > 7:
    break
else:
  print('arr안에 7보다 큰 수 없음')  
```

- `enumerate`
```python
if __name__=="__main__":
    for i,v in enumerate(['a','b','c','d']):
        print(i,v)

# i : index, v : value
```

## python 주요 라이브러리
- `import heapq` vs `import priorityQueue from queue`
  + 차이점
    - priorityQueue는 Thread-safe 하기 때문에 속도가 더 느리다. 멀티스레드 환경에서는 필수 
    - heapq는 Thread-non-safe 하기 때문에 속도가 빠르다. 알고리즘 테스트에 필수
  + heapq.heappush(min_heap, 7)
- `from itertools import permutations` # 순열 
  + permutations(arr, 3)
- `from itertools import combinations` # 조합
  + combinations(numbers, 3)
- `import re`
  + m=re.match('[^0-9]+', str)  
  + print(m.group(), m.start(), m.end())