import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 
 * dp[n] := n번째 1,2,3 합의 방법의 수 
 * 
 * dp[n-1]에서 dp[n]을 만들 수 있는 방법은 [1] 
 * dp[n-2]에서 dp[n]을 만들 수 있는 방법은 [11, 2]인데, 여기서 [11]은 중복 이므로 [2]
 * dp[n-3]에서 dp[n]을 만들 수 있는 방법은 [111, 12, 21, 3]인데, 여기서 [111, 12, 21]은 중복 이므로 [3] 
 * 즉, 각 한번씩 더해줘야한다.
 * 
 * dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
 */
public class _9095_123더하기
{
	static int N, T;
	static int dp[];
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args)
	{
		try
		{
			T = Integer.parseInt(br.readLine());
			
			for(int i = 0 ; i < T ; i ++)
			{
				N = Integer.parseInt(br.readLine());
				
				dp = new int[N+1];
				
				System.out.println(function(N));
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static int function(int n)
	{
		try
		{
			dp[1] = 1;
			dp[2] = 2;
			dp[3] = 4;
			
			for(int i = 4; i <= n ; i ++)
			{
				dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
			}
		}
		catch(Exception e)
		{
			// TODO: handle exception
		}
			
		return dp[n];
	}
}
