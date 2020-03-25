import javax.lang.model.util.ElementScanner6;

class Fibonacci
{
    public static void main(String[] args) {
        // System.out.println(fibonacci(5));    
        System.out.println(recursion(5));    
    }

    public static int fibonacci(int n) {
        int[] f = new int[n+2];
        f[0]=0;
        f[1]=1;

        for(int i = 2; i <= n ; i++)
        {
            f[i]=f[i-1]+f[i-2];
        }

        return f[n];
    }

    public static int recursion(int n)
    {
        if(n==0)
        {
            return 0;
        }
        else if(n==1)
        {
            return 1;
        }
        else
        {
            return recursion(n-1) + recursion(n-2);
        }
    }

}