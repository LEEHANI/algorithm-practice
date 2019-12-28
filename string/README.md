## 문제풀기
- 시간 초과가 난다면 stack을 써볼까? 

# Python 중요 내장 함수 
- `str(5)` # int to str
- `list('1234')` # str to list
- `''.join(['1','2','3','4'])` # list to str
- 문자열 곱셈 `str += '*'*5` # *****
- 리스트의 덧셈`[1,2,3] + [4,5] = [1,2,3,4,5]`
- `sum([1, 2, 3, 4])` # 10 
- `reversed('abcd')` # dcba  
-  `arr.index(value)` # search the list for value
- ascii
  + `ord()` #chr to ascii
  + `chr()` #ascii to chr
- `min([5, 2, 10, 1])` # 1
- 3항연산 `True if a == 2 else False`
- 정렬
  + `sorted(arr)` # return arr 
    * 정렬 조건 `sorted(arr, key=lambda x: (x[1], -x[0]))`
  + `arr.sort()` # return void
- map(function, iterable)  
  + `list(map(int, arr))` # int(all items of arr)

## python slicing 
- `s[start:end:step]`
  + `s[::-1]` 뒤에서부터 출력 # elppa

## python for
- `result = [ r for i in range(10) ]` 
  + `for i in range(10):`
            `result.append(i)`
- `array_2d = [[0 for col in range(5)] for row in range(10)]` # 10*5 배열 생성

- `enumerate`
```python
if __name__=="__main__":
    for i,v in enumerate(['a','b','c','d']):
        print(i,v)

# i : index, v : value
```