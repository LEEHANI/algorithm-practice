package queue;

import linkedList.Node;

public class LinkedListQueue 
{
	Node head;
	Node tail;
	
	public LinkedListQueue()
	{
	}
	
	public void push(int value)
	{
		Node node = new Node(value);
		
		if(head == null)
		{
			head = node;
			tail = node;
		}
		else
		{
			tail.setNext(node);
		}
	}
	
	public int pop()
	{
		if(head != null)
		{
			int value = head.getValue();
			head = head.getNext();
			
			return value;	
		}
		return 0;
	}
}
