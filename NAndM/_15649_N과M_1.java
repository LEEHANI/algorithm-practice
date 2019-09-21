import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class _15649_N과M_1
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
			
			// arr배열을 N까지 초기화
			// 편의를 위해 1부터 시작할거니 N까지 초기화
			for(int i = 1 ; i <= N; i ++)
			{
				arr.add(i);
			}
			
			permutation(result, N, M, 0);
			
			bw.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	/**
	 * 
	 * N개 중에 M개 뽑는 함수
	 * 
	 * @param result 뽑은 정수 저장 배열
	 * @param N 정수 N개 있음
	 * @param M M개 뽑기
	 * @param cnt 현재 뽑은 갯수
	 */
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
			// 예시
			// arr = {0, 1, 2, 3, 4, 5}
			// temp = 1
			// arr = {0, 2, 3, 4, 5}
			// permutation
			// arr = {0, 1, 2, 3, 4, 5}
			for(int i = 0 ; i < N; i ++)
			{
				int temp = arr.get(i);
				
				result[cnt] = temp;
				
				// 제거하지 않으면 이미 뽑았던 수를 또 뽑으므로 중복이 발생
				arr.remove(i);
				
				permutation(result, N-1, M, cnt+1);
				
				// 제거했던 수 다시 넣어주기 
				arr.add(i, temp);
			}
		}
	}
}
