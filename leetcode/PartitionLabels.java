import java.util.*;

/**
 * 칸막이를 잘 세우자 
 * 각 문자가 한 부분에서만 나올 수 있게 파티션별로 최대한 많이 나누기.
 * 예를 들어, abcabaqrq 일때, [abcaba, grg]로 나눌 수 있다.
 * 첫번째 파티션에 나오는 문자 a,b,c는 두 번째 파티션에서 나오지 않는다.
 *
 * [나의 풀이법] partitionLabels
 * letters[26]: letter counting
 * Set visited: 현재 파티션에서 등장한 문자들
 *
 * 1. s 를 한 글자씩 뽑아서 letters[26]에 counting 한다.
 * 2. s 를 한 글자씩 뽑아서 visited.add(char(i))에 넣고 letters[char(i)] 값을 하나씩 감소시킨다. visited는 현재 파티션에서 사용하고 있는 문자들이다.
 * 3. letters[char(i)] == 0 이면, 현재 파티션에서 다 사용한 문자이다.
 * 4. 현재 파티션에서 사용한 문자들인 visited 들이 더 이상 사용되지 않는지 체크한다.
 *
 * [솔루션] partitionLabelsSolution
 * last[26]: s.char(i)의 마지막 index 위치.
 * j: 현재 파티션에서 사용중인 문자열 중 마지막 index 위치.
 *
 * 1. for 문을 돌려 s 를 한 글자씩 뽑아서 해당 문자의 마지막 index 위치를 last[26]에 저장한다.
 *    예를들어, "abcabd"라면 [a:3, b:4, c:2, d:5]
 * 2. for 문을 돌려 s 를 한 글자씩 뽑는다. 사용중인 문자열 중 마지막 위치를 j에 저장해둔다. 초기값은 j=0
 *    예를들어, i:0, s.char(0):a, last[a]:3 일때, j=3. a문자열 마지막 index는 3  현재 a 문자열 등장.
 *            i:1, s.char(1):b, last[b]:4 일때, j=4. b문자열 마지막 index는 4. 현재 a,b 문자열 등장.
 *            i:2, s.char(2):c, last[c]:2 일때, j=4. c문자열 마지막 index는 2이지만 등장한 문자열(a,b,c)중 마지막 문자열 index 는 b문자열 index:4이므로 j=4. 현재 a,b,c 문자열 등장.
 *            i:3, s.char(3):a, last[a]:3 일때, j=4. a문자열 재등장. index는 3이지만 등장한 문자열(a,b,c)중 마지막 문자열 index 는 4이므로 j=4. 현재 a,b,c 문자열 등장.
 *            i:4, s.char(4):b, last[b]:4 일때, j=4  ==> i == j일때, 내가 알고 있는 문자열이 더 이상 뒤에 등장하지 않는다. 왜냐하면 last[26]에서 s.char(i)의 마지막 index 위치를 알고 있기 때문에.
 * 3. 그래서 i == j 일때 파티션이 하나 만들어진다.
 * 4. 위 내용을 반복한다.
 */
public class PartitionLabels {
    public List<Integer> partitionLabels(String s) {
        int[] letters = new int[27];

        for(int i=0; i<s.length(); i++) {
            int letter = s.charAt(i) - 'a';
            letters[letter] += 1;
        }

        List<Integer> result = new ArrayList<>();
        Set<Character> visited = new HashSet<>();
        int total = 0;

        for(int i=0; i<s.length(); i++) {
            char target = s.charAt(i);
            int letter = target - 'a';

            visited.add(target);
            letters[letter] -= 1;
            total++;

            if(letters[letter] == 0) {
                //visited 다 꺼내서 더이상 안나오는지 확인
                result.add(total);
                total=0;

                for (Character v : visited) {
                    if (letters[v - 'a'] != 0) {
                        total = result.get(result.size()-1);
                        result.remove(result.size()-1);
                        break;
                    }
                }
            }
        }
        return result;
    }

    public static List<Integer> partitionLabelsSolution(String S) {
        int[] last = new int[26];
        for (int i = 0; i < S.length(); ++i)
            last[S.charAt(i) - 'a'] = i;

        int j = 0, anchor = 0;
        List<Integer> ans = new ArrayList();
        for (int i = 0; i < S.length(); ++i) {
            char target = S.charAt(i);
            j = Math.max(j, last[target - 'a']);
            if (i == j) {
                ans.add(i - anchor + 1);
                anchor = i + 1;
            }
        }
        return ans;
    }
}
