# Array, LinkedList
## Array
- `조회`: index기반으로 조회 하므로 `O(1)`
- `삽입, 삭제`: 조회 후 원소들을 shift 해줘야 하므로 최악의 경우 `O(n)`
- 배열의 크기가 정해져있음 


## LinkedList
  + `조회`: 인덱스가 없고 노드를 찾아서 탐색해야 하므로 `O(n)`
  + `삽입, 삭제`: 노드를 새로 만들어서 `연결해주고 연결을 끊어주면 되는건 단순히 O(1)`로 가능하지만 해당 `노드를 찾아야 하므로 O(n)`
## 문제 유형, 접근 
  + 1차원, 2차원
  + 1개의 포인터(iterating), 2개의 포인터(two pointer) 
  + https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/



# 알고리즘에 사용되는 Java 지식 및 함수  
- java ArrayList의 defulat size `10`. new ArrayList(int CAPACITY)로 지정 가능.
- int result = s.charAt();
- `char[] chars = s.toCharArray();`
- `String str = String.valueOf(char);`
## Java.util.* 함수 
### Arrays
- int[] array 정렬. `Array.sort(array)`. 제자리 정렬 
- int[] array to List<Integer> 
  - ```
    list.add(Arrays.stream(array)
                .boxed()
                .collect(Collectors.toList()));
    ```

### Stack
- ```
  Stack<String> stack = new Stack<String>();
  stack.push("abc");
  stack.pop();
  stack.isEmpty();
  ```

### ArrayList
- ```
  List<String> list = new ArrayList<>();

  list.add(index, value); //index 위치에 추가 
  list.set(index, value); //index 위치에 값 변경
  ```


### Map
- ```
  Map<String, String> m = new HashMap<>();
  
  for(String key : m.keySet()) {
    ...
  }
  ```
### Math 
- `Math.min()`
- `Math.max()`