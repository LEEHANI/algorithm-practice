package linkedList;

public class LinkedList 
{
	Node head;
	
	public Node getHead() {
		return head;
	}

	public void setHead(Node head) {
		this.head = head;
	}

	public LinkedList() {
		this.head = null;
	}
	
	public void push(int value)
	{
		Node newNode = new Node(value);
		
		newNode.next = head;
		head = newNode;
	}
	
	public void push(int value, int index)
	{
		Node pointer = head;
		Node newNode = new Node(value);
		
		for(int i = 0 ; i < index-1; i ++)
		{                                                            
			pointer = pointer.next;
		}
		
		newNode.next = pointer.next;
		pointer.next = newNode;
	}
	
	public void getAllItems()
	{
		Node pointer = head;
		
		while(pointer != null)
		{
			System.out.print(pointer.value+ " -> ");
			pointer = pointer.next;
		}
		
		System.out.println("끝");
	}
	
	public boolean search(int value)
	{
		Node pointer = head; 
		
		while(pointer != null)
		{
			if(pointer.value == value)
			{
				return true;
			}
			
			pointer = pointer.next;
		}
		
		return false;
	}
	
	public void remove(int value)
	{
		Node pointer = head;
		Node parent = null;
		
		while(pointer != null)
		{
			if(pointer.value == value)
			{
				if(parent == null)
				{
					head = null;
				}
				else
				{
					parent.next = pointer.next;
				}
			}
			parent = pointer;
			pointer = pointer.next;
		}
	}
}
