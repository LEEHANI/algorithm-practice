import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class _15650_N과M_2
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
			
			for(int i = 1 ; i <= N; i ++)
			{
				arr.add(i);
			}
			
			combination(result, N, M, 0, 0);
			
			bw.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static void combination(int[] result, int N, int M, int cnt, int start)
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
			// 순서를 start로 지정해줘서 오름차순으로 택하기
			for(int i = start ; i < N; i ++)
			{
				int temp = arr.get(i);
				
				result[cnt] = temp;
				
				combination(result, N, M, cnt+1, i+1);
			}
		}
	}
}
