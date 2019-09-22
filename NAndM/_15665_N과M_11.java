import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class _15665_N과M_11
{
	static int N, M;
	static ArrayList<Integer> arr = new ArrayList<Integer>();
	static int result[];
	
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try
		{
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			result = new int[M];
			
			st = new StringTokenizer(bf.readLine());
			
			for(int i = 0 ; i < N; i ++)
			{
				arr.add(Integer.parseInt(st.nextToken()));
			}
			
			Collections.sort(arr);
			
			permutation(result, N, M, 0);
			
			bw.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static void permutation(int[] result, int N, int M, int cnt)
	{
		if(M == cnt)
		{
			try
			{
				for(int i = 0 ; i < M; i ++)
				{
					bw.write(result[i] + " ");
				}
				bw.write("\n");
				bw.flush();
			}
			catch(IOException e)
			{
				e.printStackTrace();
			}
			return;
		}
		else
		{
			int last = 0;
			
			for(int i = 0 ; i < N; i ++)
			{
				int temp = arr.get(i);
				
				if(last != temp)
				{
					result[cnt] = temp;
					
					permutation(result, N, M, cnt+1);
					
					last = result[cnt];
				}
			}
		}
	}
}
