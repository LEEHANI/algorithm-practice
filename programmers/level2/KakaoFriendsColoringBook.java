public class KakaoFriendColoringBook {
	
	public static void main(String[] args) {
		int[][] arr = {{1,1,1,0},{1,2,2,0},{1,0,0,1},{0,0,0,1},{0,0,0,3},{0,0,0,3}};
		
		solution(6,4,arr);
	}
	
	static int[] _x = {1,-1,0,0};
	static int[] _y= {0,0,-1,1};
	static int area=0;
	
	public static int[] solution(int m, int n, int[][] picture) {
		int numberOfArea = 0;
		int maxSizeOfOneArea = 0;
		int[][] visited = new int[m][n];

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (visited[i][j] == 0 && picture[i][j] != 0) {
					numberOfArea++;
					dfs(m,n, i, j, picture[i][j], visited, picture);
					
					if(maxSizeOfOneArea < area)
					{
						maxSizeOfOneArea=area;
					}
					area=0;
				}
			}
		}

		int[] answer = new int[2];
		answer[0] = numberOfArea;
		answer[1] = maxSizeOfOneArea;
		System.out.println(numberOfArea);
		System.out.println(maxSizeOfOneArea);
		return answer;
	}

	public static void dfs(int m, int n, int x, int y, int targetNum, int visited[][], int picture[][]) {
		
		visited[x][y]=targetNum;
		area++;
		
		for(int i=0;i<4;i++)
		{
			int nx=x+_x[i];
			int ny=y+_y[i];
			
			if(0<=nx && 0<=ny && nx<m && ny<n && visited[nx][ny]==0 && picture[nx][ny] == targetNum)
			{
				dfs(m,n,nx,ny,targetNum,visited,picture);
			}
		}
	}
	
	public static void p(int[][] arr)
	{
		for(int i = 0; i<arr.length;i++)
		{
			for(int j=0; j<arr[i].length; j++)
			{
				System.out.print(arr[i][j]);
			}
			System.out.println();
		}
	}
}
