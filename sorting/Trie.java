import java.util.*;

class Trie
{
    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("JOHN");  

        System.out.println(trie.select("JOHN"));  
        System.out.println(trie.select("JO"));
    }

    Node root;

    Trie()
    {
        root = new Node();
    }

    void insert(String name)
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
                node=child;
            }
        }
        node.terminal=name;
    }

    boolean select(String name)
    {
        Node node=root;
        for(int i=0;i<name.length();i++)
        {
            char target=name.charAt(i);
            
            Node child=node.children.get(target);
            if(child!=null)
            {
                if(child.terminal!=null)
                {
                    return true;
                }
                else
                {
                    node=child;
                }
            }
            else
            {
                return false;
            }
        }

        return false;
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