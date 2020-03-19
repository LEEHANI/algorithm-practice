import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
	Max Heap 구현하기 

	최대 3개 변수 비교하는 스킬 필요!
	A(index = 2), B(index = 5), C(index = 7) 중 어떤게 작은 값인지 찾아보자. 
	
	int minValue = A
	int minPosition = 2

	if(minValue < B)
		minValue = B
		minPosition = 5
	
	if(minValue < C)
		minValue = C
		minPosition = 7

 */
public class _1927 {
	public static void main(String[] args) throws Exception {
		
		int arr[] = {8,2,5,3,1};
		
		MinHeap heap = new MinHeap();
		
		for(int i = 0 ; i < arr.length ; i++)
		{
			heap.push(arr[i]);
		}
			
		System.out.println(heap.pop()); // 1
		System.out.println(heap.pop()); // 2
		System.out.println(heap.pop()); // 3
		System.out.println(heap.pop()); // 5
		System.out.println(heap.pop()); // 8
		System.out.println(heap.pop()); // exception
	}
	
	static class MinHeap
	{
		ArrayList<Integer> arr;
		int index=0;
		
		public MinHeap()
		{
			arr=new ArrayList<Integer>();
			arr.add(-1);
		}
		
		public void print()
		{
			for(int i = 1; i < arr.size(); i ++)
			{
				System.out.print(arr.get(i) + " ");
			}
			System.out.println();
		}
		
		public int getIndex()
		{
			return index;
		}
		
		public void push(int value)
		{
			index++;
			arr.add(value);
			
			int child = index;
			int parent=child/2;
			
			while(arr.get(parent) > value && parent >= 1)
			{
				arr.set(child, arr.get(parent));
				arr.set(parent, value);
				
				child=parent;
				parent=child/2;
			}
		}
		
		public int pop() throws Exception
		{
			if(index <= 0)
			{
				throw new Exception();
			}
			
			int target = arr.get(1);
			
			heapify();
			
			return target;
		}
		
		public void heapify()
		{
			int parent = 1;
			
			if(index > 1)
			{
				arr.set(parent, arr.get(index));
				arr.remove(index);
				
				while(parent*2 < index)
				{
					int left = parent*2;
					int right = parent*2+1;
					int minValue = arr.get(parent);
					int minPosition = parent;
					
					if(minValue > arr.get(left))
					{
						minValue=arr.get(left);
						minPosition=left;
					}
					
					if(right<index && minValue > arr.get(right))
					{
						minValue=arr.get(right);
						minPosition=right;
					}
					
					if(minPosition == parent)
					{
						break;
					}
					
					arr.set(minPosition, arr.get(parent));
					arr.set(parent, minValue);
					parent=minPosition;
						
				}
			}

			index--;			
		}
	}
}

