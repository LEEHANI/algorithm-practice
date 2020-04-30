class _4811
{
    public static void main(String[] args) {
        System.out.println(sol(20, 0));
    }

    static int sol(int n, int m)
    {
        //비정상 종료
        if(m<0 || n<0)
        {
            return 0;
        }
        
        //정상 종료
        if(n==0)
        {
            return 1;
        }

        //일반적
        return sol(n-1, m+1) + sol(n, m-1);
    }
}