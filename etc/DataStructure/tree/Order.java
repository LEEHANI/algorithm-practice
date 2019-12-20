package tree;

public class Order 
{
	int arr[][];
	
	public Order(int arr[][])
	{
		this.arr = arr;
	}
	
	public void preOrder(int start)
	{
		if(start == -1)
		{
			return;
		}
		
		System.out.println(start);
		preOrder(arr[start][0]);
		preOrder(arr[start][1]);
	}
	
	public void inOrder(int start)
	{
		if(start == -1)
		{
			return;
		}
		
		inOrder(arr[start][0]);
		System.out.println(start);
		inOrder(arr[start][1]);
	}
	
	public void postOrder(int start)
	{
		if(start == -1)
		{
			return;
		}
		
		postOrder(arr[start][0]);
		postOrder(arr[start][1]);
		System.out.println(start);
	}
}
