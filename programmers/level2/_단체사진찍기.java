
public class _단체사진찍기 {
    public static void main(String[] args) {
		String[] data = {"N~F=0", "R~T>2"};
//		String[] data = {"M~C<2", "C~M>1"};
		solution(1, data);
	}
	
	static int size;
	static char[] info;
	static boolean[] visited;
	static int answer;
	
	public static int solution(int n, String[] data)
	{
		size=8;
		info = new char[]{'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
		visited = new boolean[size];
		answer=0;
		
		// permutation[i] = 'C'   <==> i번째 자리에 C가 있다.
		char[] result = new char[size];
		permutation(0, result, data);
		return answer;
	}
	
	public static void permutation(int depth, char[] result, String[] data)
	{
		if(depth==size)
		{
			for(String str:data)
			{
				char a=str.charAt(0);
				char b=str.charAt(2);
				
				int aIndex=0;
				int bIndex=0;
				
				int num=Integer.parseInt(str.substring(4));
				
				for(int i=0;i<size;i++)
				{
					if(result[i]==a)
					{
						aIndex=i;
					}
					
					if(result[i]==b)
					{
						bIndex=i;
					}
				}
				
				if(str.charAt(3) == '=')
				{
					if(Math.abs(aIndex-bIndex)-1==num)
					{
						continue;
					}
					else
					{
						return;
					}
				}
				else if(str.charAt(3) == '>')
				{
					if(Math.abs(aIndex-bIndex)-1>num)
					{
						continue;
					}
					else
					{
						return;
					}
				}else if(str.charAt(3) == '<')
				{
					if(Math.abs(aIndex-bIndex)-1<num)
					{
						continue;
					}
					else
					{
						return;
					}
				}
			}
			
			answer++;
			return;
		}
		else
		{
			for(int i=0;i<size;i++)
			{
				if(visited[i]==false)
				{
					visited[i]=true;
					result[depth]=info[i];
					permutation(depth+1,result,data);
					visited[i]=false;
				}
			}
		}
	}
}