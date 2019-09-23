Binary Search
===
이진탐색은 정렬된 데이터에 대해서 log(N) 복잡도를 가지는 탐색 기법이다. 


### 예시   

오름차순으로 정렬된 배열이 있을 때, 이진 탐색을 이용하여 target `19`를 찾아보자.   

| 1  | 5  | 10  | 14  | `19`  | 22  | 24  |
|---|---|---|---|---|---|---|   
<br/>

#### 첫번째 시도   

| 1  | 5  | 10  | `14`  | `19`  | 22  | 24  |
|---|---|---|---|---|---|---|  



배열의 가운데 값인 `14`를 택한다.   
`14` < `19` 이므로 target은 선택한 값보다 오른쪽이 있다.    
그러므로 `14`보다 오른쪽에 있는 배열만 탐색하면 된다.     


#### 두번째 시도  
| `19`  | `22`  | 24  |
|---|---|---|   


배열의 가운데 값인 `22`를 택한다.    
`22` > `19` 이므로 target은 선택한 값보다 왼쪾에 있다.    
그러므로 `22`보다 왼쪽에 있는 배열만 탐색하면 된다.    


#### 세번째 시도   
| `19`  |
|---|    


배열의 가운데 값인 `19`를 택한다.   
`19` == target 이므로 탐색을 종료한다.    

     
<br/>
<br/>
### 소스 코드

```
binarySearch(int arr[], start, end, target) {
  int mid = (start + end) / 2
  
  if (start > end)
    return -1 // not found
  
  if (arr[mid] == target)
    return mid // found
  if (arr[mid] < target)
    return binarySearch(arr, mid+1, end, target)
  else if (arr[mid] > target)
    return binarySearch(arr, start, mid-1, target)
}
```
