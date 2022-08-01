import java.util.*;

/**
 * 중복을 허용
 * candidates를 정렬 후 combination 하는게 포인트 
 */
public class CombinationSum {
  Set<List<Integer>> answer = new HashSet<>();

  public List<List<Integer>> combinationSum(int[] candidates, int target) {
    Arrays.sort(candidates);
    combination(candidates, target, new ArrayList<>(), 0);
    return new ArrayList<>(answer);
  }

  public void combination(int[] candidates, int target, List<Integer> result, int sum) {
    if (sum > target) {
      return;
    }

    if (sum == target) {
      ArrayList<Integer> list = new ArrayList<>(result);
      answer.add(list);
      return;
    }

    for (int i = 0; i < candidates.length; i++) {
      // 시간 초과 방지 
      if (result.size() >= 1 && result.get(result.size() - 1) > candidates[i]) {
        continue;
      }
      result.add(candidates[i]);
      combination(candidates, target, result, sum + candidates[i]);
      result.remove(result.size() - 1);
    }
  }
}
