package stack;

/**
 * 배열 공간 낭비
 * 빠름 
 *
 */
public class ArrayStack 
{
	int arr[] = null;
	int point = 0;
	
	public ArrayStack(int size)
	{
		this.arr = new int[size];
	}
	
	public void push(int value)
	{
		arr[point] = value;
		point ++;
		
		System.out.println("push " + value);
	}
	
	public void getAllItems()
	{
		for(int i = 0 ; i < point ; i ++)
		{
			System.out.print(arr[i] + " -> ");
		}
		System.out.println("끝");
	}
	
	public Boolean isEmpty()
	{
		if(point > 0)
		{
			return false;
		}
		
		return true;
	}
	
	public int pop()
	{
		if(!isEmpty())
		{
			int value = arr[point-1];
			point --;
			
			System.out.println("pop " + value);
			return value;
		}
		
		return 0;
	}
	
}
