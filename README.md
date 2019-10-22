# Algorithm Practice
코딩테스트 준비

## 문제 풀기 전 생각 
- 시간 복잡도 생각하기
- 공간 복잡도 생각하기 
- 자료구조 선택하기 
- (정렬)

## 자료구조 
- array, ArrayList
- Queue, Stack
- Map
- Graph, Tree

## 알고리즘 풀이 방법

- Greedy Algorithm
- N and M
- DP(Dynamic Programming)
- DFS, BFS
- Tree
- Binary Search

## Java  
입출력 시 Scanner, Sysout대신 BufferedReader, BuffredWriter를 쓰자  
+ 입력 Scanner, System.out.println  
```  
Scanner scan = new Scanner(System.int);

int n = scan.nextInt();

scan.nextLine();

String str = scan.nextLine();

System.out.println(n + ", " + str);
```  

+ 출력 BufferedReader, BuffredWriter  
```  
BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

try
{
    int n = Integer.parseInt(bf.readLine());
    String str = bf.readLine();

    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    bw.write(n + "\n");
    bw.write(str + "\n");

    bw.flush(); // 남아있는 데이터 모두 출력
    bw.close(); // 스트림 닫기

}
catch(Exception e)
{
	// TODO: handle exception
}
```  
<hr>

## Python   
코테를 보다가.. 자바대신 파이썬을 쓰기로 결심함  
파이썬 선택 이유   

- 시험 볼 때 대괄호```{}```, 세미콜론 ```;``` 쓰는 시간 조차 아까움  
- ```for```문 작성이 오래걸림  
- ```문자열``` 처리가 어려움   
- ```입출력``` 때 손이 많이 감 

아직 익숙지 않아서 가독성도 떨어지고 코드 짜는데 오래 걸리지만! 계속 연습중  


- 입력 input(), sys.stdin.readline().strip()
```
import sys

cnt = int(input())
N, M = map(int, sys.stdin.readline().strip().split())
```
- 출력
```
print(N,M)
```