import java.util.*;

/**
 * Map<Integer, Integer> dp = new HashMap<>(); //key 값일 때, 사용된 최소한의 동전 갯수. dp의 메모리를 효율적으로 사용하기 위해 array 대신 map을 사용
 * Map<Integer, Integer> co = new HashMap<>(); //coins 초기값
 * 
 * [3, 4] 13
 * 맨 처음 coins[i] 값을 1로 설정. 
 * 그 후 1~13 for문 돌면서 coins 값 빼기. coins 값 뺀 나머지 값은 내가 이전에 최소한의 동전 갯수를 알고 있으므로 그 값을 사용. 
 * 예를들어 i=5일때, 5-3=2 --> 2일때 최소한의 동전 갯수를 알고있음 
 *        i=5일때, 5-4=1 --> 1일때 최소한의 동전 갯수를 알고있음 
 *
 *        i=6일때, 6-3=3 --> 3일때 최소한의 동전 갯수를 알고있음 
 *        i=6일때, 6-4=2 --> 2일때 최소한의 동전 갯수를 알고있음 
 */
public class CoinChange {
  public static int coinChange(int[] coins, int amount) {
    // coinChange(new int[] { 186, 419, 83, 408 }, 6249);

    if (amount == 0)
      return 0;

    Arrays.sort(coins);
    Map<Integer, Integer> dp = new HashMap<>();  //key일 때, 사용된 최소한의 동전 갯수
    Map<Integer, Integer> co = new HashMap<>();  //coins 초기값

    for (Integer c : coins) {
      dp.put(c, 1);
      co.put(c, 1);
    }

    for (int i = 1; i <= amount; i++) {
      // i의 최대 만들수 있는 값
      for (int j = 0; j < coins.length; j++) {
        int target = i - coins[j];

        if (target <= 0)
          continue;

        Integer min = dp.get(target);

        if (min == null || min == 0) {
          dp.put(target, 0);
          continue;
        }

        if (co.get(i) == null) {
          if (dp.get(i) != null) {
            dp.put(i, Math.min(dp.get(i), 1 + min));
          } else {
            dp.put(i, 1 + min);
          }
        }
      }
    }
    return dp.getOrDefault(amount, -1);
  }
}
