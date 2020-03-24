public class LeftRotation
{
    public static void main(String[] args) {
        int[] a = {1,2,3,4,5};
        rotLeft(a,4);
	}
	
	static int gcd(int a, int b)
	{
		int temp = 0;
		
		while(b != 0)
		{
			temp=a;
			a=b;
			b=temp%b;
		}		
		return a;
	}
	
    static int[] rotLeft(int[] a, int d) {
    	
    	int size = a.length;
    
    	int gcd = gcd(size, d);
    	
        for(int i = 0 ; i < gcd; i++)
        {
            int temp = a[i];

            int index = i;

            int target = (index + d)%size;
            
            while(target != i)
            {
                a[index] = a[target];
    
                index = target;
                target = (index + d)%size;
            }
            a[index] = temp;
        }
    	
    	return a;
    }
}