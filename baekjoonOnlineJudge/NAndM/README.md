
## Permutation
- 자바로 순열 구현하기 (+ visited[] 대신 bit visited 사용해보기)

```java
public class Permutation {
	static final int size = 8;
	static int[] permutation = new int[size];
	static int[] visited = new int[size];
	static int answer=0;
	
	public static void main(String[] args) {
		permutation(0,permutation);
		System.out.println(answer);
		answer=0;
		permutation(0,permutation, 0);
		System.out.println(answer);
	}
	
	public static void permutation(int depth, int[] permutation)
	{
		if(depth==size)
		{
			answer++;
			return;
		}
		
		for(int i = 0 ; i < size; i ++)
		{
			if(visited[i] == 0)
			{
				permutation[depth] = i;
				visited[i]=1;
				permutation(depth+1, permutation);
				visited[i]=0;
			}
		}
	}
	
	public static void permutation(int depth, int[] permutation, int visited)
	{
		if(depth==size)
		{
			answer++;
			return;
		}
		
		for(int i = 0 ; i < size; i++)
		{
			if(((visited>>i) & 1) == 0) // 방문 안했으면
			{
				permutation[depth] = i;
				permutation(depth+1, permutation, visited | (1<<i));				
			}
		}
		
	}
}

```