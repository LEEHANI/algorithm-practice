import java.util.*;

public class GroupAnagrams {
  public List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> answer = new ArrayList<>();
    Map<String, List<String>> m = new HashMap<>();

    for (String s : strs) {
      char[] chars = s.toCharArray();
      Arrays.sort(chars);
      String key = String.valueOf(chars);

      if (m.get(key) == null) {
        List<String> list = new ArrayList<>();
        list.add(s);
        m.put(key, list);
      } else {
        m.get(key).add(s);
      }
    }

    for (String key : m.keySet()) {
      answer.add(m.get(key));
    }

    return answer;
  }
}
