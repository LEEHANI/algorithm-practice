package queue;

public class ArrayQueue 
{
	int arr[];
	int head = 0;
	int tail = 0;
	
	public ArrayQueue(int size)
	{
		arr = new int[size];
	}
	
	public void push(int value)
	{
		if(size() == tail)
		{
			System.out.println("full!!!");
			return;
		}
		
		System.out.println("push " + value);
		arr[tail] = value;
		tail++;
	}
	
	public int pop()
	{
		if(head == tail)
		{
			return 0;
		}
		System.out.print("pop ");
		return arr[head++];
	}
	
	public int size()
	{
		return arr.length;
	}
}
