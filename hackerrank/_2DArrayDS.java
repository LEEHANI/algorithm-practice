import java.io.*;
import java.util.*;

public class _2DArrayDS {

    // Complete the hourglassSum function below.
static int hourglassSum(int[][] arr) {
        final int MIN = -9;

        int max = MIN*7 ;
        int i = arr.length;
        int j = arr[0].length;
        
        int sum = 0;
        
        for(int n = 0; n<i-2; n++)
        {
            
            for(int m = 0; m<j-2; m++)
            {
                
                sum+= arr[n][m] + arr[n][m+1] + arr[n][m+2];
                sum+= arr[n+1][m+1];
                sum+= arr[n+2][m] + arr[n+2][m+1] + arr[n+2][m+2];

                if(sum > max)
                {
                    max=sum;
                }
                sum = 0;
            }
        }
        
        return max;
    }
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int result = hourglassSum(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
