import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 2xn 직사각형을 타일로 채우는 방법은 2x(n-1)과 2x(n-2)의 방법을 보면 된다. 
 * 
 * 2x(n-1)에서 2xn를 만드려면 1x2를 하나 세우면 된다. 하지만 이 방법은 2xn에서 이미 셌다.     
 * 2x(n-2)에서 2xn를 만드려면 1x2(2개), 2x1(2개), 2x2(1개)로 3가지 방법이 있다. 하지만 1x2(2개) 방법은 2xn에서 이미 셌다.     
 * 
 * 그러므로 
 * 2xn = 2xn-1 + 2x(2xn-2) 
 * 
 * dp[1], dp[2]는 초기값 필요. 그 다음부턴 식으로 구할 수 있음.
 * 
 * dp[1] = 1 1x2 1개
 * dp[2] = 3 1x2(2개), 2x1(2개), 2x2(1개) 
 */
public class _11727_2xn타일링_2
{
	static int N;
	static int dp[];
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args)
	{
		try
		{
			N = Integer.parseInt(br.readLine());
			
			dp = new int[N+1];
			
			System.out.println(bottomUp(N));
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static int bottomUp(int n)
	{
		try
		{
			dp[0] = 0;
			dp[1] = 1;
			dp[2] = 3;
			
			for(int i = 3 ; i <= N; i ++)
			{
				dp[i] = (dp[i-1] + 2*dp[i-2])%10007; // 오버플로우 방지를 위해 계산할 때 10007를 나눠줘야함! 
			}
			
		}
		catch(Exception e)
		{
//			e.printStackTrace(); 꼭 주석하자 !!! 아니면 런타임 에러 발생함
		}
		
		return dp[n];
	}
}
