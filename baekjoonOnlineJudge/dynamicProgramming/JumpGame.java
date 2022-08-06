import java.util.*;

public class JumpGame {
  // canJump(new int[]{3,2,1,0,4});

  public static boolean canJump(int[] nums) {
    Stack<Integer> stack = new Stack<Integer>(); //갈 수 있으면 index 값을 stack에 넣기 
    int size = nums.length;
    boolean[] dp = new boolean[size];
    for (int i = 0; i < size; i++) {
      // 거꾸로
      int last = size - i - 1;
      // 맨마지막이면 그냥 넣기
      if (last == size - 1) {
        dp[last] = true;
        stack.push(last);
        continue;
      }

      int s = stack.peek();
      if (nums[last] >= s - last) {
        stack.push(last);
        dp[last] = true;
      }
    }
    return dp[0];
  }
}
