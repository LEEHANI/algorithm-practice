import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 기존 피보나치와 다르게 n번째에 0과 1을 몇번씩 썼는지 각각 저장해야한다. 
 * Count 클래스를 만들어서 이를 해결함
 */
public class _1003_피보나치함수
{
	static int N, T;
	static Count dp[];
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args)
	{
		try
		{
			T = Integer.parseInt(br.readLine());
			
			for(int i = 0 ; i < T ; i ++)
			{
				N = Integer.parseInt(br.readLine());
				
				dp = new Count[N+1];
				
				Count count = fibonacci(N);
				
				System.out.println(count.zero + " " + count.one);
			}
			
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static Count fibonacci(int n)
	{
		try
		{
			dp[0] = new Count(1, 0);
			dp[1] = new Count(0, 1);
			
			for(int i = 2; i <= n ; i ++)
			{
				Count count1 = dp[i-1];
				Count count2 = dp[i-2];
				
				dp[i] = new Count(count1.zero + count2.zero, count1.one + count2.one); 
			}
		}
		catch(Exception e)
		{
			
		}
		
		return dp[n];
	}
	
	static class Count
	{
		int zero;
		int one;
		
		Count(int zero, int one)
		{
			this.zero = zero;
			this.one = one;
		}
	}
}
