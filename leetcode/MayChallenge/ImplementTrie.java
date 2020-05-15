public import java.util.HashMap;

public class ImplementTrie {
	
	Node root = null;
	
    /** Initialize your data structure here. */
    public ImplementTrie() {
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node node = root;
        
    	for(int i = 0 ; i<word.length(); i++)
    	{
    		char target = word.charAt(i);
    		
    		if(node.children.get(target) == null)
    		{
    			Node newNode = new Node(word.charAt(i));
    			
    			node.children.put(target, newNode);
    			
    			node=newNode;
    		}
    		else
    		{
    			node=node.children.get(target);
    		}
    	}
    	
    	node.terminal=word;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
    	Node node = root;
    	
    	for(int i = 0 ; i<word.length(); i++)
    	{
    		char target=word.charAt(i);
    		if(node.children.get(target)!=null)
    		{
    			node=node.children.get(word.charAt(i));
    		}
    		else
    		{
    			return false;
    		}
    	}
    	
    	if(node.terminal != null && node.terminal.equals(word))
    	{
    		return true;
    	}
    	
        return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
    	Node node = root;
    	
    	for(int i=0; i<prefix.length(); i++)
    	{
    		char target = prefix.charAt(i);
    		
    		if(node.children.get(target) != null)
    		{
    			node=node.children.get(target);
    		}
    		else
    		{
    			return false;
    		}
    	}
    	
        return true;
    }
    
    class Node
    {
    	char c;
    	HashMap<Character, Node> children = new HashMap<>();
    	String terminal;
    	
    	public Node(char c)
    	{
    		this.c = c;
    	}
    	
    	public Node(){    	}
    }
    
    public static void main(String[] args) {
		ImplementTrie tr = new ImplementTrie();
		
		tr.insert("app");
		boolean result = tr.search("app");
//		System.out.println(result);
		result=tr.search("ap");
//		System.out.println(result);
		result=tr.startsWith("b");
		System.out.println(result);
	}
}