

class DavisStaircase
{
    private static int answer = 0;
    public static void main(String[] args) {
        s("",10);
        System.out.println((answer));
        System.out.println(s2(10));
    }

    public static void start(String s, int n)
    {
        // 출력
        if(n%2==0){
            System.out.println(s);
        }
        // 비즈니스 로직
        if(n>0)
        {
            start(s+"*",n-1);
        }
        
    }   

    public static void s(String s, int n)
    {
        if(n>0){
            s(s+"3 ", n-3);
            s(s+"2 ", n-2);
            s(s+"1 ", n-1);
        }
        if(n==0){
            System.out.println(s);
            answer +=1;
        }
        else{
            return;
        }
    }

    //n을 표현하는 방법의 개수를 반환.
    public static int s2(int n){
        if(n==0){
            return 1;
        }
        if(n>0){
            return s2(n-3) + s2(n-2) + s2(n-1);
        }
        else{
            return 0;
        }
    }
}