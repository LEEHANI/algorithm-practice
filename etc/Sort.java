import java.util.Arrays;
import java.util.List;

public class Sort {
	public static void main(String[] args) {
		int[] arr = {20, 12, 10, 15, 2};
		
		selectionSort(arr);
		p(arr);
	}
	
	public static void selectionSort(int arr[])
	{
		for(int i = 0 ; i < arr.length-1 ; i ++)
		{
			for(int j = i+1 ; j < arr.length ; j ++)
			{
				if(arr[i] > arr[j])
				{
					int swap = arr[i];
					arr[i]=arr[j];
					arr[j]=swap;
				}
			}
		}
	}
	
	public static void p(int arr[])
	{
		for(int i = 0 ; i < arr.length ; i ++ )
		{
			System.out.print(arr[i] + " ");
		}
	}

}
