package queue;

import java.util.Stack;

/**
 * 
 *
 */
public class TwoStackMakeQueue 
{
	Stack<String> s1 = new Stack<String>();
	Stack<String> s2 = new Stack<String>();
	
	public TwoStackMakeQueue()
	{
	}
	
	public void push(String c)
	{  
		s1.push(String.valueOf(c));
	}
	
	public String pop()
	{
		if(!s2.isEmpty())     
		{
			return s2.pop();
		}
		
		while(!s1.isEmpty())
		{
			s2.push(s1.pop());
		}
		
		if(s2.isEmpty())
		{
			return null;
		}
		
		return s2.pop();
	}
}
