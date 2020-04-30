/**
    주어진 배열을 K만큼 Shift하는 알고리즘 만들기
 */
public class ShiftArray {

    /**
        배열을 k만큼 오른쪽으로 shift하기
     */
	public static void shiftArray(int k, int arr[]) {
		int size = arr.length;
		int gcd = gcd(k, size);

		for (int j = 0; j < gcd; j++) {
			int target = arr[j];
			int i = j;
			
			do {
				i = (i + k) % size;
				
				int swap = arr[i];
				arr[i] = target;
				target = swap;
				
			} while (i != j);
		}
	}

	public static int gcd(int a, int b) {
		int tmp = a;

		while (b != 0) {
			tmp = a;

			a = b;
			b = tmp % b;
		}
		return a;
	}

	public static void p(int arr[]) {
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
	}

	public static void main(String[] args) {
		int arr[] = { 0, 1, 2, 3, 4, 5, 6 };

		shiftArray(2, arr);

		p(arr);
	}
}
