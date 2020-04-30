import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class _1463_1로만들기
{
	static int n;
	static int dp[]; // 정수 n이 주어졌을 때, n을 1로 만드는 최소횟수
	
	// -1, %3, %2 다 해봐서 최솟값을 dp에 저장해놓기!
	// -1, %3, %2 하면 연산 한번 했으므로 +1 꼭 해줘야함!!
	// dp[n] = dp[n-1] + 1  <-- n-1(전 단계)의 최솟값 + 1( -1로 한번 연산을 진행했으므로 1 더해줘야한다)   
	// if(n %2 == 0) dp[n] = dp[n/2] + 1
	// if(n %3 == 0) dp[n] = dp[n/3] + 1
	
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		try
		{
			n = Integer.parseInt(bf.readLine());
			
			dp = new int[n+1];
			
//			bw.write(topDown(n) + "\n");
			
//			bw.write(bottomUp(n) + "\n");
			
			bw.write(bfs(1) + "\n");
			
			bw.flush();
				
		    bw.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static int bfs(int s)
	{
		Queue<Integer> q = new LinkedList<Integer>();
		
		dp[s] = 0;
		q.add(s);
		
		while(!q.isEmpty())
		{
			int v = q.poll();
			
			if(v == n)
			{
				return dp[v];
			}
			
			if(dp[v+1] == 0)
			{
				dp[v+1] = dp[v] + 1;
				q.add(v+1);
			}
			
			//배열의 인덱스범위 && 방문 안했는지 확인
			if(v*2 <= n && dp[v*2] == 0)
			{
				dp[v*2] = dp[v] + 1;
				q.add(v*2);
			}

			if(v*3 <= n && dp[v*3] == 0)
			{
				dp[v*3] = dp[v] + 1;
				q.add(v*3);
			}
		}
		
		return 0;
	}
	
	public static int bottomUp(int s)
	{
		if(s == 1)
		{
			return 0;
		}
		
		if(s == 2 || s == 3)
		{
			return 1;
		}
		
		dp[1] = 0;
		dp[2] = 1;
		dp[3] = 1;
		
		for(int i = 4; i <= s ; i ++)
		{
			int temp1 = dp[i-1] + 1;
			int temp2 = i%3 == 0 ? dp[i/3] + 1 : (1<<30); // 이 문제에서 가장 큰 숫자! 1<<30
			int temp3 = i%2 == 0 ? dp[i/2] + 1 : (1<<30);
			
			dp[i] = Math.min(temp1, Math.min(temp2, temp3));
		}
		
		return dp[s];
	}
	
	public static int bottomUpVersion2(int n)
	{
		try
		{
			dp[1] = 0;
			dp[2] = 1;
			dp[3] = 1;
			
			for(int i = 4; i <= n ; i ++)
			{
				dp[i] = dp[i-1] +1;
				
				if(i % 2 == 0)
				{
					dp[i] = Math.min(dp[i], dp[i/2]+1);
				}
				
				if(i % 3 == 0)
				{
					dp[i] = Math.min(dp[i], dp[i/3]+1);
				}
			}
		}
		catch(ArrayIndexOutOfBoundsException e)
		{
			// n이 3이하면 에러 발생하므로 방지용임
		}
		
		return dp[n];
	}
	
	// 시간초과
	public static int topDown(int s)
	{
		if(s == 1)
		{
			return dp[s];
		}
		
		// 굳이 안해줘도 알아서 계산
//		if(s == 2 || s == 3)
//		{
//			dp[s] = 1;
//			
//			return dp[s];
//		}
		
		dp[s] = topDown(s - 1) + 1;
		
		if(s % 3 == 0)
		{
			return dp[s] = Math.min(dp[s], topDown(s/3) + 1);
		}
		
		if(s % 2 == 0)
		{
			return dp[s] = Math.min(dp[s], topDown(s/2) + 1);
		}
		
		return dp[s];
	}
}
