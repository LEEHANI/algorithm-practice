import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

/**
 * 첫번째 시도
 * arr[n][1] 을 정렬한다.
 * for문을 0부터n까지 
 * arr[i][1]가 만약 5라면
 * arr[i+1][0] 가 5 이상일때 까지 찾기 arr[i+1][1]을 다음 타깃으로 설정 
 * 결과: 시간초과
 * 
 * 두번째 시도
 * arr[n][1] 을 정렬한다.
 * arr[n]을 맵에 저장해서 몇번째 i에 있는지 위치 파악하기.
 * 문제점: 회의 시작시간과 끝나는 시간이 같을 때를 고려하지 못함..
 * 
 * ==============================================================================
 * 
 * 최대한 회의를 많이 하기 위해 "회의 시간은 짧아야 한다"라는 생각에 초점을 맞췄었는데 ....... 좀 다르게 생각해야한다.
 * 회의가 일찍 끝나는 시간을 택해야한다.  
 * [1,4] [3,5] 가 있을 때 첫번째걸 택해야한다. 
 * 왜냐하면 [4:N]이 [5:N] 보다 회의를 더 많이 할 수 있기 때문이다. 그러므로 arr[n][1]에 대해 정렬해야한다. 
 *  
 * 근데 여기서 끝이 아니다.. 시작시간과 끝나는 시간이 같을 수 있기 때문에 arr[n][0] 도 정렬을 해야한다. 
 * 
 * 예를 들어, 회의가 [1,1],[1,2],[2,2] 라고 했을 때, 끝나는 시간만으로 정렬할 경우
 * discuss = [[1,1],[2,2],[1,2]] 가 될 수있고, 우리는 회의의 수를 2라고 출력하게 된다.
 * 따라서 회의의 시작 시간에 대해서도 정렬이 필요하다.
 * 즉, discuss =[[1,1],[1,2],[2,2]] 로 정렬되어있어야, 올바른 회의 수를 카운트할 수 있다.
 *  
 * 매우 어렵다,, 정렬도 어렵다,,  
 */
public class _1931_회의실배정
{
	static int N, answer;
	static int arr[][];
	
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try
		{
			N = Integer.parseInt(bf.readLine());
			
			arr = new int[N][2];
			
			for(int i = 0 ; i < N ; i ++)
			{
				StringTokenizer st = new StringTokenizer(bf.readLine());
				
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				arr[i][0] = a;
				arr[i][1] = b;
			}
			
			Arrays.sort
			(
				arr, new Comparator<int[]>() 
				{ 
		            public int compare(int[] start, int[] end) 
		            {
		                if(start[1]==end[1]){
		                    return Integer.compare(start[0], end[0]);
		                }
		                return Integer.compare(start[1], end[1]);
		            } 
				}
			);
			
			for(int i = 0 ; i < N ; i ++)
			{
				System.out.println(arr[i][0] + " " + arr[i][1]);
			}
			
			answer = 1;
			
			int temp = arr[0][1];
			
			for(int i = 1 ; i < N ; i ++)
			{
				if(arr[i][0] >= temp)
				{
					temp = arr[i][1];
					answer += 1; 
				}
			}
			
			System.out.println(answer);
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
}
