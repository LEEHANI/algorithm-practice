package linkedList;

import queue.ArrayQueue;
import queue.LinkedListQueue;
import queue.TwoStackMakeQueue;
import stack.ArrayStack;
import stack.LinkedListStack;
import stack.Maze;

public class Main 
{
	public static void main(String[] args) 
	{
		
//		linkedListTest();
		
//		arrayStack();
//		linkedListStack();
		
//		maze();
		
//		arrayQueue();
//		linkedListQueue();
		
//		twoStackMakeQueue();
		
		int arr[] = {4, 3, 1, 2, 5};
		insertSort(arr);
	}
	
	public static void insertSort(int arr[])
	{
		for( int i = 1 ; i < arr.length; i ++)
		{
			int temp = arr[i];
			
			int j = 0;
			for (j = i-1 ; j >= 0 ; j--)
			{
				if(arr[j] < temp)
				{
					break;
				}
				
				arr[j+1] = arr[j];
			}
			arr[j+1] = temp;
		}
		
		print(arr);
	}
	
	public static void print(int arr[])
	{
		for ( int i = 0 ; i < arr.length ; i ++)
		{
			System.out.print(arr[i] +  " ");
		}
	}

	
	public static void twoStackMakeQueue()
	{
		TwoStackMakeQueue q = new TwoStackMakeQueue();
		
		q.push("h");
		q.push("e");
		q.push("l");
		q.push("0");
		System.out.println(q.pop());
		q.push("!");
		System.out.println(q.pop());
		System.out.println(q.pop());
		System.out.println(q.pop());
		System.out.println(q.pop());
		System.out.println(q.pop());
		System.out.println(q.pop());
		System.out.println(q.pop());
	}
	
	public static void linkedListQueue()
	{
		LinkedListQueue q = new LinkedListQueue();
		q.push(2);
//		q.push(7);
		System.out.println(q.pop());
		System.out.println(q.pop());
		q.push(5);
		System.out.println(q.pop());
	}
	
	public static void arrayQueue()
	{
		ArrayQueue q = new ArrayQueue(3);
		q.push(2);
		System.out.println(q.pop());
		System.out.println(q.pop());
		q.push(5);
		System.out.println(q.pop());
	}
	
	public static void maze()
	{
		int arr[][] = 
		{
			{1, 0, 1, 1, 1, 1},
			{1, 0, 1, 0, 1, 1},
			{1, 0, 1, 0, 1, 0},
			{1, 1, 1, 0, 1, 1}
		};
		
		Maze maze = new Maze(4, 6, arr);
		maze.bfsIterative(0, 0);
//		maze.bfsRecursive(0, 0);
	}
	
	public static void linkedListStack()
	{
		LinkedListStack stack = new LinkedListStack();
		
		stack.push(5);
		stack.push(10);
		stack.pop();
		stack.pop();
		stack.pop();
	}
	
	public static void arrayStack()
	{
		ArrayStack stack = new ArrayStack(5);
		
		stack.push(2);
		stack.push(10);
		stack.pop();
		stack.pop();
		// empty_pop
		stack.pop();
		stack.getAllItems();
		stack.push(5);
		stack.getAllItems();
	}
	
	public static void linkedListTest()
	{
		LinkedList ll = new LinkedList();
		// 
		ll.push(5);
		ll.push(8);
		ll.getAllItems();
		//
		ll.push(3, 1);
		ll.getAllItems();
		//
		System.out.println(ll.search(8));
		System.out.println(ll.search(99));
		//
		ll.remove(5);
		ll.getAllItems();
		ll.remove(8);
		ll.getAllItems();
		ll.remove(8);
		ll.getAllItems();
	}
}
