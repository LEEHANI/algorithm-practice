import java.util.Stack;

class MinStack {

	Stack<Integer> s;
	Stack<Integer> minStack;
	
    /** initialize your data structure here. */
    public MinStack() {
        s=new Stack<>();
        minStack=new Stack<>();
    }
    
    public void push(int x) {
        s.push(x);
        
        if(!minStack.isEmpty() && minStack.peek()>=x)
        {
        	minStack.push(x);
        }
        if(minStack.isEmpty())
        {
        	minStack.push(x);
        }
    }
    
    public void pop() {
        int temp = s.pop();
        
        if(!minStack.isEmpty() && minStack.peek() == temp)
        {
        	minStack.pop();
        }
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {
    	int temp=Integer.MAX_VALUE;
    	if(!minStack.isEmpty())
    	{
    		temp=minStack.peek();
    	}
    	
    	if(!s.isEmpty())
    	{
    		temp=Math.min(s.peek(), temp);
    	}
        return temp;
    }
    
    public static void main(String[] args) {
		MinStack m1 = new MinStack();
		m1.push(0);
		m1.push(1);
		m1.push(0);
		System.out.println(m1.getMin());
		m1.pop();
		System.out.println(m1.getMin());
	}
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */