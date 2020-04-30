
class Abbreviation
{
    public static void main(String[] args) {
        System.out.println(abbreviation("a", "B"));
    }

    // Complete the abbreviation function below.
    static String abbreviation(String a, String b) {

        int dp[][] = new int[a.length()+1][b.length()+1];
        dp[0][0] = 1;

        for(int i=0; i<a.length(); i++){
            for(int j=0; j<=b.length();j++){
                if(dp[i][j] == 1){
                    char charA = a.charAt(i);
                    if('a' <= charA && charA <= 'z'){
                        dp[i+1][j] = 1;
                    }
                    if(j+1<=b.length()){
                        char charB = b.charAt(j);
                        if(((charA == charB) || (charA - 'a' == charB - 'A'))){
                            dp[i+1][j+1] = 1;
                        }
                    }
                }
            }
        }

        for(int i=1;i<a.length()+1; i++){
            for(int j=1;j<b.length()+1;j++){
                System.out.print(dp[i][j]+" ");
            }
            System.out.println();
        }

        if(dp[a.length()][b.length()] ==1){
            return "YES";
        }
        else{
            return "NO";
        }
    }
}