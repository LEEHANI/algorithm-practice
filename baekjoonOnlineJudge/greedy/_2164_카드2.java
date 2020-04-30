import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class _2164_카드2
{
	static int n;
	static int arr[];
	
	// 2019.09.16
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try
		{
			n = Integer.parseInt(bf.readLine());
			
			Queue<Integer> q = new LinkedList<Integer>();
			
			for(int i = 1 ; i <= n; i ++)
			{
				q.add(i);
			}
			
			while(q.size() != 1)
			{
				int size = q.size();
				
				for(int i = 1 ; i <= size; i ++)
				{
					if(i % 2 == 1)
					{
						q.remove();
						q.add(q.remove());
					}
				}
			}
			System.out.println(q.peek());
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
}
