import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class _1316_그룹단어체커
{
	static int n;
	
	// 2019.09.15
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		try
		{
			n = Integer.parseInt(bf.readLine());
			
			int cnt = 0;
			
			for(int i = 0 ; i < n ; i ++)
			{
				Map<String, Boolean> m = new HashMap<String, Boolean>();
				
				String str = bf.readLine();
				
				for(int j = 0 ; j < str.length() ; j ++)
				{
					String temp = str.substring(j, j+1);
					
					if(m.get(temp) == null)
					{	
						m.put(temp, true);
					}
					else
					{
						// 연속하는 단어인지 체크
						if(!temp.equals(str.substring(j-1, j)))
						{
							cnt --;
							break;
						}
					}
				}
				cnt ++;
			}
			
			System.out.println(cnt);
		}
		catch(Exception e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}


