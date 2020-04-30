import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// class Main
// {
//     public static void main(String[] args) {
        
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
//         try
//         {
//             int c = Integer.parseInt(br.readLine());
//             for(int i = 0 ; i < c ; i++)
//             {
//                 Trie trie = new Trie();
//                 int n = Integer.parseInt(br.readLine());

//                 boolean result = true;
//                 for(int j=0;j<n;j++)
//                 {
//                     result = trie.insert(br.readLine());
                    
//                     if(result==false)
//                     {
//                         break;
//                     }
//                 }
//                 System.out.println(result);
//             }
//         }
//         catch(Exception e)
//         {
//             // TODO: handle exception
//         }
//     }
// }

class Trie
{
    public static void main(String[] args) {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                
        try
        {
            int c = Integer.parseInt(br.readLine());
            for(int i = 0 ; i < c ; i++)
            {
                Trie trie = new Trie();
                int n = Integer.parseInt(br.readLine());
                String info[] = new String[n];
                
                for(int j=0;j<n;j++)
                {
                    info[j]=br.readLine();
                }
                
                Arrays.sort(info);
                
                boolean result = true;
                String answer = "YES";
                
                for(int j=0;j<n;j++)
                {
                    result = trie.insert(info[j]);
                    if(result==false)
                    {
                        answer="NO";
                    }
                }
                System.out.println(answer);
            }
        }
        catch(Exception e)
        {
            // TODO: handle exception
        }
    }

    Node root;

    Trie()
    {
        root = new Node();
    }

    boolean insert(String name)
    {
        Node node = root;

        for(int i=0;i<name.length();i++)
        {
            char target=name.charAt(i);

            Node child = node.children.get(target);
            
            if(child == null)
            {
                Node newNode = new Node(target);
                node.children.put(target, newNode);
                node=newNode;
            }
            else
            {
            	if(child.terminal != null)
            	{
            		return false;
            	}
                node=child;
            }
            
        }
        node.terminal=name;

        return true;
    }
}

class Node
{
    char value;
    Map<Character, Node> children = new HashMap<Character, Node>();
    String terminal;

    public Node(){}
    Node(char value)
    {
        this.value = value;
    }
}