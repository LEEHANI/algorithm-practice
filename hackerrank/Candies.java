/**
 * 숫자가 커지는건 상관없지만 커졌다가 작아지는 순간 문제가 발생 
 * 
 * [2 6 8 9 4 3 2 1] 일 때,
 * 1, 2, 3, 4 ... 로 캔디를 주게 되는데, [9]일때 대처를 어떻게 해야할지 고민이 매우 생길것이다.
 * [9] 다음에는 숫자가 줄어드니까 캔디를 기존에서 -1해야하나? 아니면 1개를 줘야하나?
 * [9] 다음에 하락하는 숫자의 갯수를 알수만 있다면... 해결될텐데 ... 그렇다고 for문을 돌려서 찾자니 최악의 경우 n번 찾아봐야한다.. 
 * 
 * [결론]
 * 숫자가 올라가면서 캔디를 하나씩 주면 상관없지만 내려갈 때 문제가 되므로.. 뒤로도 캔디를 세서 내리막길을 오르막길로 만들어버리고, 둘 중 max 값을 찾으면 된다.
 * 
 */
class Candies
{
    public static void main(String[] args) {
        int arr[] = {2,6,8,9,4,3,2,1};
        candies(0, arr);    
    }

    static long candies(int n, int[] arr) {
        long answer = 0;
        long[][] dp = new long[2][arr.length];
        dp[0][0]=1;
        dp[1][arr.length-1]=1;
        int j=0;
        for(int i = 1 ; i < arr.length; i++)
        {
            j=arr.length-i-1;

            if(arr[i]>arr[i-1])
            {
                dp[0][i]=dp[0][i-1]+1;
            }
            else
            {
                dp[0][i]=1;
            }

            if(arr[j] > arr[j+1])
            {
                dp[1][j]=dp[1][j+1]+1;
            }
            else
            {
                dp[1][j]=1;
            }
        }

        for(int i = 0 ; i < arr.length; i++)
        {
            long max = dp[0][i];

            if(max < dp[1][i])
            {
                max = dp[1][i];
            }

            answer+=max;
        }

        return answer;
    }

    static void p(long arr[])
    {
        for(int i = 0; i<arr.length; i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}