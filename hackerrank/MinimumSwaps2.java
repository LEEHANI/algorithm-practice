public class MinimumSwaps2
{
    public static void main(String[] args) {
        int[] a = {4,3,1,2};
        
        System.out.println(minimumSwaps(a));
    }
    static int minimumSwaps(int[] arr) {
        int answer = 0;
        
        int start = 0;
        int end = arr.length-1;

        while(start<end)
        {
            p(arr);

            if(arr[start]==start+1)
            {
                start+=1;
                continue;
            }

            if(arr[end]==end-1)
            {
                end-=1;
                continue;
            }

            swap(arr, start, arr[start]-1);
            answer++;
        }
        
        return answer;
    }

    public static void swap(int a[], int index1, int index2)
    {
        int temp = a[index1];
        a[index1] = a[index2];
        a[index2] = temp;
    }

    static void p(int a[])
    {
        for(int i = 0 ; i<a.length; i++)
        {
            System.out.print(a[i]+" ");
        } 
        System.out.println();
    }
}