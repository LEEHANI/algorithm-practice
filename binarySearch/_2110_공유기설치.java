import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _2110_공유기설치
{
	static int N;
	static int C;
	static int answer;
	static int arr[];
	
	// 2019.09.18
	// 공유기의 간격이 최대가 되도록 하는 문제!
	// 간격을 BS를 이용해 찾아간다
	// 공유기으 ㅣ갯수가 많을 수록 간격은 좁아지며, 반대로 공유기의 갯수가 적을수록 간격은 넓어진다. 
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try
		{
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			N = Integer.parseInt(st.nextToken());
			C = Integer.parseInt(st.nextToken());
			
			arr = new int[N];
			
			for(int i = 0 ; i < N ; i ++)
			{
				int temp = Integer.parseInt(bf.readLine());
				
				arr[i] = temp;
			}
			
			Arrays.sort(arr);
			
			// 1 ~ arr[N-1]-arr[0] 사이에 정답이 있다.
			System.out.println(binarySearch(1, arr[N-1]-arr[0]));
			
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static int binarySearch(int s, int e)
	{
		int mid = (s + e) /2;
		
		int result = count(mid);
		
		if(s > e)
		{
			return mid;
		}
		
		if(result >= C)
		{
			return binarySearch(mid+1, e);
		}
		else if(result < C)
		{
			return binarySearch(s, mid-1);
		}
			
		return 0;
	}
	
	public static int count(long mid)
	{
		int total = 1;
		
		int v = arr[0];
		
		for(int i = 1; i < arr.length ; i ++)
		{
			int temp = arr[i];
			
			if(temp >= (v+mid))
			{
				total += 1;
				v = temp;
			}
		}
		
		return total;
	}
}