import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Hackerrank {
	public static void main(String[] args) {
//		int []arr = {2,3,4,2,3,6,8,4,5};
		int []arr = {10,20,30,40,50};
		
		System.out.println(activityNotifications(arr, 3));
	}
	
	static double mid(int[] counting, int d)
	{
		double mid=0;
		
		int countIndex = 0;
		
		if(d%2==0)
		{
			boolean index1=true;
			boolean index2=true;
			
			for(int i = 0; i<=200; i++)
			{
				countIndex+=counting[i];
				
				if(index1 && countIndex >= d/2)
				{
					mid+=i;
					index1=false;
				}
				
				if(index2 && countIndex >= d/2+1)
				{
					mid+=i;
					index2=false;
					break;
				}
			}
			System.out.println(mid);
			return mid/2D;
		}
		else
		{
			for(int i = 0; i<=200; i++)
			{
				countIndex+=counting[i];
				
				if(countIndex > d/2)
				{
					return i;
				}
			}
		}
		
		return 0;
	}
	
    static int activityNotifications(int[] expenditure, int d) {
    	int[] counting = new int[201];
        
        for(int i = 0 ; i < d ; i ++ )
        {
        	counting[expenditure[i]] += 1;
        }
        
        int size = expenditure.length;
        int notification = 0;
        
        for(int i = d; i < size; i++)
        {
//            for(int j = i-d ; j < i ; j ++)
//            {
//                temp[k++] = expenditure[j];
//            }
//
//            Arrays.sort(temp);
            double mid = mid(counting, d);
            	
        	System.out.println(mid);
            
            if(expenditure[i] >= mid*2)
            {
            	notification ++;
            }
            
            counting[expenditure[i-d]] -= 1;
            counting[expenditure[i]] += 1;
        }
        
        return notification;
    }
    
    public static void p(int arr[])
	{
		for(int i = 0 ; i < arr.length ; i ++ )
		{
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}
}
