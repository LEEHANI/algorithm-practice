import java.util.*;

/**
 * 파티션을 잘 나누자.
 * 앞을 고정시키고 나머지는 작게 분할하자.
 * prefix | remain
 */
public class PalindromePartitioning {
    
    static Set<List<String>> answer = new HashSet<>();
    public static void main(String[] args) {
        System.out.println(partition("aabaa"));
    }

    public static Set<List<String>> partition(String s) {
        if(isPalindrome(s)) {
            answer.add(Arrays.asList(s));
        }
        rec(s, new ArrayList<>());
        return answer;
    }

    public static void rec(String s, List<String> result) {
        if(s.length()<=1) {
            return;
        }

        //prefix, remain이 palindrome 인지 check
        //prefix가 팰린드롬이면 remain은 계속 쪼개기
        for(int i=1; i<s.length(); i++) {
            String prefix = s.substring(0, i);
            String remain = s.substring(i);

            boolean palindrome = isPalindrome(prefix);
            if (!palindrome) {
                continue;
            }
            result.add(prefix);

            //remain이 팰린드롬이면, 하나 찾음.
            if(isPalindrome(remain)) {
                result.add(remain);
                answer.add(new ArrayList<>(result));
                result.remove(result.size()-1);
            }
            rec(remain, result);
            result.remove(result.size() - 1);
        }
    }

    public static boolean isPalindrome(String s) {
        for(int i=0; i<s.length()/2; i++) {
            if(s.charAt(i) != s.charAt(s.length()-1-i)) {
                return false;
            }
        }
        return true;
    }
}
