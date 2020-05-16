class oddEvenLinkedList {
    public ListNode oddEvenList(ListNode head) {
    	
    	if(head == null || head.next == null)
    	{
    		return head;
    	}
    	
    	ListNode oddHead = head;
        ListNode odd = head;
        ListNode evenHead = head.next;
        ListNode even = head.next;
        
        while(true)
        {
        	if(even.next != null)
        	{
        		odd.next=even.next;
        		System.out.println("odd"+odd.val+", "+odd.next.val);
        		odd=odd.next;
        		if(odd.next != null)
        		{
        			even.next=odd.next;
        			System.out.println("even"+even.val+", "+even.next.val);
        			even=even.next;    
        			continue;
        		}
        		else
        		{
        			even.next=null;
        			break;
        		}
        	}
        	else
        	{
        		break;
        	}
        }
        
        odd.next=evenHead;
        
        return oddHead;
    }
}