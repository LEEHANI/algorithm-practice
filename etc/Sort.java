public class Sort 
{
	public static void main(String[] args) 
	{
//		int[] arr = {20, 12, 10, 15};
		
		int[] arr = {2,1};
		
//		selectionSort(arr);
//		bubbleSort(arr);
//		insertSort(arr);

//		mergeSort(arr, 0, arr.length-1, new int[arr.length]);
		
//		int[] heap_arr = {-1, 20, 12, 10, 15, 9, 1, 100};
//		heapSort(heap_arr);
		
		quickSort(arr, 0, arr.length-1);
		
		p(arr);
	}
	
	/**
	 * [시간복잡도]
	 * O(n^2)
	 */
	public static void selectionSort(int arr[])
	{
		for(int i = 0 ; i < arr.length-1 ; i++)
		{
			for(int j = i+1 ; j < arr.length ; j++)
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
	
	/**
	 * [시간복잡도]
	 * O(n^2)
	 */
	public static void bubbleSort(int arr[])
	{
		for(int i = 0 ; i < arr.length-1 ; i++)
		{
			for(int j = 0 ; j < arr.length-i-1 ; j++)
			{
				if(arr[j] > arr[j+1])
				{
					int swap=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=swap;
				}
			}
		}
	}
	
	
	/**
	 * [시간복잡도]
	 * 평균: O(n^2)
	 * 최선의 경우: O(n-1)
	 */
	public static void insertSort(int arr[])
	{
		for(int i = 1; i < arr.length ; i++)
		{
			int target = arr[i];
			
			for(int j = i-1; j>=0 ; j--)
			{
				if(arr[j] > target)
				{
					arr[j+1] = arr[j];
				}
				else // stable
				{
					arr[j+1] = target;
					break;
				}
				
				if(j==0) {
					arr[j] = target;
				}
			}
		}
	}
	
	
	// ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
	
	/**
	 * [시간복잡도]
	 * O(nlogn)
	 */
	public static void mergeSort(int arr[], int start, int end, int temp[])
	{
		if(start < end)
		{
			int mid = (start+end)/2;
			
			mergeSort(arr, start, mid, temp);
			mergeSort(arr, mid+1, end, temp);
			
			merge(arr, start, mid, end, temp);
		}
	}
	
	public static void merge(int arr[], int start, int mid, int end, int temp[])
	{
		int i = start;
		int j = mid + 1;
		int k = start;
		
		while( i <= mid && j <= end)
		{
			if( arr[i] <= arr[j])
			{
				temp[k] = arr[i];
				i++;
			}
			else
			{
				temp[k] = arr[j];
				j++;
			}
			k++;
		}
		
		while(i <= mid)
		{
			temp[k] = arr[i];
			k++;
			i++;
		}
		
		p(temp);
		
		while(j <= end)
		{
			temp[k] = arr[j];
			k++;
			j++;
		}
		
		for(int q = start; q <= end; q ++)
		{
			arr[q] = temp[q];
		}
	}
	
	public static void heapSort(int arr[])
	{
		int last = arr.length-1;
		int lastParent = last/2;
		
		for(int i = lastParent; i >= 1; i--)
		{
			heapify(arr, i, last);
		}
		
		int[] temp = new int[arr.length];
		
		for(int i = 1; i < arr.length; i++)
		{
			temp[i] = heapPop(arr, last--);
		}
		
		for(int i = 1; i < arr.length; i++)
		{
			arr[i] = temp[i];
		}
				
	}
	
	public static int heapPop(int arr[], int last)
	{
		int max = arr[1];
		arr[1] = arr[last];
		last --;
		
		heapify(arr, 1, last);
		
		return max;
	}
	
	public static void heapify(int arr[], int parent, int last)
	{
		while(parent*2 <= last)
		{
			int maxValue = arr[parent];
			int maxPosition = parent;
			
			if(maxValue <= arr[parent*2])
			{
				maxValue = arr[parent*2];
				maxPosition = parent*2;
			}
			
			if(parent*2+1 <= last && maxValue <= arr[parent*2+1])
			{
				maxValue = arr[parent*2+1];
				maxPosition = parent*2+1;
			}
			
			if(parent == maxPosition)
			{
				break;
			}
			
			int temp = arr[parent];
			arr[parent] = maxValue;
			arr[maxPosition] = temp;
			
			parent = maxPosition;
		}
	}
	
	public static void quickSort(int arr[], int start, int end)
	{
		if(start < end)
		{
			int pivot = partition(arr, start, end);
//		partition(arr, 0, arr.length-1);
			
			quickSort(arr, start, pivot-1);
			quickSort(arr, pivot+1, end);
		}
	}
	
	public static int partition(int arr[], int start, int end)
	{
		int i = start;
		int j = end;
		int p = arr[start];
		i++;
		
		int temp = 0;
		
		while(i<=j)
		{
			while(i<=j && arr[i] <= p)
			{
				i++;
			}
			
			while(i<=j && arr[j] > p)
			{
				j--;
			}

			if(i<=j) {
				temp = arr[i];
				arr[i]=arr[j];
			 	arr[j]=temp;
			}
		}
		
		arr[start] = arr[j];
		arr[j] = p;
		
		return j;
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
