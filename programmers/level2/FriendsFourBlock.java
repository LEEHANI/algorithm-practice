
public class FriendsFourBlock {
    public static void main(String[] args) {
		String[] board = {"CCBDE", "AAADE", "AAABF", "CCBBF"}; // 14
//		String[] board = {"TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"};
//		String[] board = {"TTTTTT", "TTTTTT", "TTTTTT", "TTTTTT", "TTTTTT", "TTTTTT"};
//		String[] board = {"CCBDE", "AAADE", "CCBDE", "AAADE", "CCBDE", "AAADE"};
//		String[] board = {"AA", "AA", "CC", "AA", "AA", "DD"}; // 8
		solution(4,5,board);
	}

	public static int solution(int m, int n, String[] board) {
		int answer = 0;

		char boards[][] = new char[m][n];
		int visited[][] = new int[m][n];

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				boards[i][j] = board[i].charAt(j);
			}
		}
		
		int temp = -1;
		while(temp != 0)
		{
			temp = checkBlock(visited, boards, m, n);
			removeBlock(visited, boards, m,n);
//			p(visited);
//			System.out.println();
//			p(boards);
//			System.out.println();
//			System.out.println();
			answer+=temp;
//			visited = new int[m][n];
			init(visited);
		}
		
		System.out.println(answer);
//		
		return answer;
	}
	
	public static void removeBlock(int visited[][], char[][] boards, int m, int n) {
		for (int y = 0; y < n; y++) {
			int start=-1;
			int end=-1;
			Stack<int[]> s = new Stack<>();
			
			for (int x =m-1; x >= 0; x--) {
				if (visited[x][y] == 1) {
					
					if(start<0)
					{
						start=x;
					}
					end=x;
				}
				
				if((visited[x][y] == 0 || x==0) && end>=0)
				{
//					break;
					s.add(new int[]{start, end});
					start=-1;
					end=-1;
				}
			}
			
			System.out.println("s size:"+s.size());
			while(!s.isEmpty())
			{
				System.out.println(start+"    "+end);
				int[] temp = s.pop();
				start=temp[0];
				end=temp[1];
				
				if(start>=0 && end>=0)
				{
					for (int x = start; x >= 0; x--) {
						if(end-1 >= 0)
						{
							boards[x][y]=boards[--end][y];
						}
						else
						{
							boards[x][y]='0';
						}
					}
				}
			}
		}
	}
	
	public static int checkBlock(int visited[][], char [][]boards, int m, int n)
	{
		int removeBlock = 0;
		int []_x= {0,1,1};
		int []_y= {1,1,0};
		
		for (int x = 0; x < m; x++) {
			for (int y = 0; y < n-1; y++) {
				if(boards[x][y] != '0')
				{
					char target=boards[x][y];
					
					boolean _4block = true;
					for(int i=0; i<3; i++)
					{
						int nx=x+_x[i];
						int ny=y+_y[i];
						if(nx>=0 && ny>=0 && nx<m && ny<n && boards[nx][ny]==target)
						{
							continue;
						}
						else
						{
							_4block=false;
							break;
						}
					}
					
					if(_4block)
					{
						if(visited[x][y]==0)
						{
							removeBlock++;
						}
						if(visited[x+_x[0]][y+_y[0]]==0)
						{
							removeBlock++;
						}
						if(visited[x+_x[1]][y+_y[1]]==0)
						{
							removeBlock++;
						}
						if(visited[x+_x[2]][y+_y[2]]==0)
						{
							removeBlock++;
						}
						
						visited[x][y]=1;
						visited[x+_x[0]][y+_y[0]]=1;
						visited[x+_x[1]][y+_y[1]]=1;
						visited[x+_x[2]][y+_y[2]]=1;
					}
				}
			}
		}
		
		return removeBlock;
	}
	
	public static void init(int[][] visited)
	{
		for(int i=0;i<visited.length;i++)
		{
			for(int j=0;j<visited[0].length;j++)
			{
				visited[i][j]=0;
			}
		}
	}

	public static void p(char[][] arr )
	{
		for(int i=0;i<arr.length;i++)
		{
			for(int j=0;j<arr[0].length;j++)
			{
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
	}
	
	public static void p(int[][] arr )
	{
		for(int i=0;i<arr.length;i++)
		{
			for(int j=0;j<arr[0].length;j++)
			{
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
	}
}