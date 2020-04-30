/**
 * dp[i] arr i번째일 때의 최댓값.
 * 
 * dp[2] 일때 초기값이 음수가 나올 수 있기 때문에 주의해야함.
 * subset은 {}이 가능하므로 가장 작은 sum은 0이다. 즉, 배열이 음수로 이루어져 있어서 아무것도 선택하지 않는 경우
 */
class MaxArraySum
{
    public static void main(String[] args) {
        int arr[] = 
                    // {3,7,4,6,5}
                    // {2,1,5,8,4}
                    // {3,5,-7,8,10}
                    {1}
                    ;
        System.out.println(maxSubsetSum(arr));
    }

    // Complete the maxSubsetSum function below.
    static int maxSubsetSum(int[] arr) {
        int[] dp = new int[arr.length+1];
        int answer=arr[0];

        try 
        {
            dp[0]=arr[0];
            dp[1]=arr[1];
            dp[2]= max(arr[0], arr[2], arr[0]+arr[2]);
    
            if(answer < dp[1])
            {
                answer = dp[1];
            }
    
            if(answer < dp[2])
            {
                answer = dp[2];
            }
            
        } catch (Exception e) {
        }

        for(int i = 3; i < arr.length; i++)
        {
            if(arr[i]>0)
            {
                dp[i] = max(dp[i-2], dp[i-3], 0)+arr[i];
            }
            else
            {
                dp[i] = max(dp[i-1], dp[i-2], dp[i-3]);
            }

            if(answer < dp[i])
            {
                answer = dp[i];
            }
        }

        return answer;
    }

    static int max(int a, int b, int c)
    {
        int max = a;

        if(max < b)
        {
            max = b;
        }

        if(max < c)
        {
            max = c;
        }

        return max;
    }

    static void p(int a[])
    {
        for(int i = 0; i < a.length; i++)
            System.out.print(a[i] + " ");
        System.out.println();
    }
}