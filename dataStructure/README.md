# Array, LinkedList
## Array
  + 조회: index기반으로 조회 하므로 O(1)
  + 삽입, 삭제: 조회 후 원소들을 shift 해줘야 하므로 최악의 경우 O(n) 
  + 배열의 크기가 정해져있음 
## LinkedList
  + 조회: 인덱스가 없고 노드를 찾아서 탐색해야 하므로 O(n)
  + 삽입, 삭제: 노드를 새로 만들어서 연결해주고 연결을 끊어주면 되는건 단순히 O(1)로 가능하지만 해당 노드를 찾아야 하므로 O(n)
## 문제 유형, 접근 
  + 1차원 2차원
  + 1개의 포인터(iterating), 2개의 포인터 
  + https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/