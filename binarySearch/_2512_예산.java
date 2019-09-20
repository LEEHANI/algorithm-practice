import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _2512_예산
{
	static int N;
	static long M;
	static int arr[];
	
	// 2019.09.20
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try
		{
			N = Integer.parseInt(bf.readLine());
			
			arr = new int[N];
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			for(int i = 0 ; i < N ; i ++)
			{
				arr[i] = Integer.parseInt(st.nextToken());
			}
			
			M = Integer.parseInt(bf.readLine());
			
			Arrays.sort(arr);
			
			System.out.println(binarySearch(1, arr[N-1]));
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static long binarySearch(long start, long end)
	{
		long mid = (start + end)/2;
		
		if(start > end)
		{
			return mid;
		}
		
		long result = budget(mid);
		
		if(result < 0)
		{
			return binarySearch(start, mid-1);
		}
		else if(result >= 0)
		{
			return binarySearch(mid+1, end);
		}
		
		return 0;
	}
	
	public static long budget(long mid)
	{
		long remain = M;
		long sum = 0;
		
		for(int i = 0 ; i < N ; i ++)
		{
			long temp = mid - arr[i];
			
			if(temp >= 0)
			{
				sum += arr[i];
			}
			else
			{
				sum += mid;
			}
		}
		
		return (remain - sum);
	}
}
