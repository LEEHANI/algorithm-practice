import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;

class _1181
{
    public static void main(String[] args) {
        String[] arr;  
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        try
        {
            int n = Integer.parseInt(br.readLine());
            arr = new String[n];
            for(int i = 0 ; i < n ; i++)
            {
                arr[i]=br.readLine();
            }

            sort(arr);
        }
        catch(Exception e)
        {
            // TODO: handle exception
        }
    }

    static void sort(String[] arr)
    {
        int D = findLength(arr);
        LinkedList<String>[] counting = new LinkedList[27];
        for(int i = 0; i<counting.length; i++)
        {
            counting[i] = new LinkedList<String>();
        }

        for(int d = 0 ; d < D; d++)
        {
            countingSort(arr, d, counting);
        }

        String[] newArray = new String[arr.length];

        String target = arr[0];
        newArray[0]=target;
        int k = 1;
        System.out.println(target);
        for(int i = 1 ; i<arr.length; i++)
        {
            if(arr[i].equals(target))
            {
                continue;
            }
            else
            {
                target = arr[i];
                newArray[k++]=target;
                System.out.println(target);
            }
        }

        // p(counting);
        // p(newArray);
    }

    static void countingSort(String[] arr, int d, LinkedList<String>[] counting)
    {
        for(int i = 0 ; i<arr.length; i++)
        {
            String target = arr[i];
            int targetLength = target.length();

            if(targetLength-1 < d)
            {
                counting[0].add(target);
            }
            else
            {
                counting[(int)target.charAt(targetLength-d-1)-'a'+1].add(target);
            }
        }

        int k=0;

        for(int i = 0 ; i<counting.length; i++)
        {
            while(!counting[i].isEmpty())
            {
                arr[k++]=counting[i].pop();
            }
        }
    }

    static void p(LinkedList<String>[] a)
    {
        for(int i = 0; i<a.length; i++)
        {
            System.out.println(a[i]);
        }
    }

    static void p(String[] a)
    {
        for(int i = 0; i<a.length; i++)
        {
            System.out.println(a[i]);
        }
    }

    static int findLength(String[] a)
    {
        int d=0;

        for(int i = 0 ; i < a.length; i++)
        {
            if(a[i].length() > d)
            {
                d = a[i].length();
            }
        }

        return d;
    }
}