package stack;

import java.util.Stack;

public class Maze {
	
	int x;
	int y;
	int dx[] = {1, -1, 0, 0};
	int dy[] = {0, 0, -1, 1};
	boolean visited[][];
	int arr[][];
	boolean finish = false;
			
	public Maze(int x, int y, int arr[][])
	{
		this.x = x;
		this.y = y;
		visited = new boolean[x][y];
		this.arr = arr;
	}
	
	public class Point
	{
		public int x;
		public int y;
		
		public Point(int x, int y)
		{
			this.x = x;
			this.y = y;
		}
		
	}
	
	public void print()
	{
		for( int i = 0 ; i < x ; i ++ )
		{
			for(int j = 0 ; j < y; j ++)
			{
				if(visited[i][j])
				{
					System.out.print(1);
				}
				else
				{
					System.out.print(0);
				}
				System.out.print(" ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public void bfsIterative(int startX, int startY)
	{
		Stack<Point> stack = new Stack<Point>();
		visited[startX][startY] = true;
		stack.add(new Point(startX, startY));
		
		while(!stack.isEmpty())
		{
			Point point = stack.pop();
			print();
			System.out.println(point.x + " " + point.y);
			
			if((point.x+1) == x && (point.y+1) == y)
			{
				return;
			}
			
			for(int i = 0 ; i < 4 ; i ++)
			{
				int nx = point.x + dx[i];
				int ny = point.y + dy[i];
				
				if(nx>=0 && ny>=0 && nx<x && ny<y)
				{
					if(arr[nx][ny] == 1 && visited[nx][ny] == false)
					{
						visited[nx][ny] = true;
						stack.add(new Point(nx, ny));
					}
				}
			}
		}
	}
	
	public void bfsRecursive(int startX, int startY)
	{
		if(finish)
		{
			return;
		}
		
		if((startX+1) == this.x && (startY+1) == this.y)
		{
			print();
			finish = true;
		}
		
		visited[startX][startY] = true;
		
		for(int i = 0 ; i < 4; i ++)
		{
			int nx = startX + dx[i];
			int ny = startY + dy[i];
			
			if(nx >= 0 && ny >= 0 && nx < x && ny < y)
			{
				if(arr[nx][ny] == 1 && visited[nx][ny] == false)
				{
					bfsRecursive(nx, ny);
				}
			}
		}
	}
}
