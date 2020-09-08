public class DetectCapital {
    public static void main(String[] args) {
        boolean flaG = detectCapitalUse("FG");
        System.out.println(flaG);
    }

    public static boolean detectCapitalUse(String word) {
        char first = word.charAt(0);
        int big = 0;
        int small = 0;
        if('a'<= first && first<='z') small++;

        for (int i = 1; i < word.length(); i++) {
            char charAt = word.charAt(i);
            if('A'<= charAt && charAt<='Z') big++;
            else small++;
            if(big==0 || small==0) continue;
            return false;
        }

        return true;
    }
}
