import java.util.*;

public class CombinationSum2 {
  // System.out.println(combinationSum2(new int[]{1,1,2,5,6,7,10}, 8));
  // System.out.println(combinationSum2(new int[]{1,1,1,1,1,1},3));

  public static List<List<Integer>> combinationSum2(int[] candidates, int target) {
    Set<List<Integer>> answer = new HashSet<>();
    Arrays.sort(candidates);
    combination(candidates, target, new ArrayList<>(), answer, 0, 0);

    return new ArrayList<>(answer);
  }

  public static void combination(int[] candidates, int target, List<Integer> picks, Set<List<Integer>> answer, int sum,
      int index) {
    if (sum > target) {
      return;
    }

    if (sum == target) {
      answer.add(new ArrayList<>(picks));
      return;
    }

    for (int i = index; i < candidates.length; i++) {
      // 키포인트: 중복체크 ***
      if (i > index && candidates[i] == candidates[i - 1])
        continue;
      picks.add(candidates[i]);
      combination(candidates, target, picks, answer, sum + candidates[i], i + 1);
      picks.remove(picks.size() - 1);
    }
  }
}
