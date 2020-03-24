import java.util.*;

public class BubbleSort {

    // Complete the countSwaps function below.
    static void countSwaps(final int[] a) {
        int swapCount = 0;

        for(int i = 0; i < a.length-1; i ++)
        {
            for(int j = 0; j < a.length-1-i; j++)
            {
                if(a[j] > a[j+1])
                {
                    final int temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                    swapCount++;
                }
            }
        }
        System.out.println("Array is sorted in "+swapCount+" swaps.");
        System.out.println("First Element: "+a[0]);
        System.out.println("Last Element: "+a[a.length-1]);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(final String[] args) {
        final int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        final int[] a = new int[n];

        final String[] aItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            final int aItem = Integer.parseInt(aItems[i]);
            a[i] = aItem;
        }

        countSwaps(a);

        scanner.close();
    }
}
