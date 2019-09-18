import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1654_랜선자르기
{
	static int K, N;
	static long arr[];
	
	// 2019.09.17
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try
		{
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			K = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			
			arr = new long[K];
			
			long max = 0;
			
			for(int i = 0 ; i < K ; i ++)
			{
				long temp = Integer.parseInt(bf.readLine());
				
				arr[i] = temp;
				
				if(temp > max)
				{
					max = temp;
				}
			}
			
			System.out.println(binarySearch(1, max));
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static long binarySearch(long s, long e)
	{
		long mid = (s + e) /2;
		
		long result = cut(mid);
		
		if(s > e)
		{
			return mid;
		}
		
		if(result >= N)
		{
			return binarySearch(mid+1, e);
		}
		else if(result < N)
		{
			return binarySearch(s, mid-1);
		}
			
		return 0;
	}
	
	public static long cut(long num)
	{
		long total = 0;
				
		for(int i = 0 ; i < K ; i ++)
		{	
			total += arr[i]/num;
		}
		
		return total;
	}
}