import java.util.*;

public class Permutations {
  static List<List<Integer>> answer = new ArrayList<>();
  public static void main(String[] args) {
    permute(new int[] { 1, 2, 3 });
  }

  public static List<List<Integer>> permute(int[] nums) {
    int size = nums.length;
    permutation(nums, new int[size], new boolean[size], size, 0);
    return answer;
  }

  public static void permutation(int[] nums, int[] result, boolean[] visited, int size, int depth) {
    if (size == depth) {
      answer.add(Arrays.stream(result)
          .boxed()
          .collect(Collectors.toList()));
    }

    for (int i = 0; i < size; i++) {
      if (visited[i]) {
        continue;
      }

      visited[i] = true;
      result[depth] = nums[i];
      permutation(nums, result, visited, size, depth + 1);
      visited[i] = false;
    }
  }  
}
