import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2805_나무자르기
{
	static int N;
	static long M;
	static long arr[];
	
	// 2019.09.18
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try
		{
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			arr = new long[N];
			
			long max = 0;
			
			st = new StringTokenizer(bf.readLine());
			
			for(int i = 0 ; i < N ; i ++)
			{
				long temp = Integer.parseInt(st.nextToken());
				
				arr[i] = temp;
				
				if(temp > max)
				{
					max = temp;
				}
			}
			
			System.out.println(binarySearch(0, max));
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
		
		if(result >= M)
		{
			return binarySearch(mid+1, e); 
		}
		else if(result < M)
		{
			return binarySearch(s, mid-1);
		}
			
		return 0;
	}
	
	public static long cut(long num)
	{
		long total = 0;
				
		for(int i = 0 ; i < N ; i ++)
		{	
			long temp = arr[i] - num;
			
			if(temp > 0)
			{
				total += temp;
			}
		}
		
		return total;
	}
}