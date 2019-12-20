package stack;

import linkedList.LinkedList;
import linkedList.Node;

/**
 * 앞에서부터 넣고 빼면 O(1) 만큼 걸림
 * 가변적
 *
 */
public class LinkedListStack 
{
	LinkedList link = new LinkedList();
	
	public LinkedListStack(){}
	
	public void push(int value)
	{
		link.push(value);
		link.getAllItems();
	}
	
	public int pop()
	{
		Node head = link.getHead();
		
		if(head != null)
		{
			int value = head.getValue();
			link.setHead(head.getNext());
			System.out.println(value);
			
			return value;
		}
		
		System.out.println(0);
		return 0;
	}
}
