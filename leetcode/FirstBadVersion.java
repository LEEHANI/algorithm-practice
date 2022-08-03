/**
 * int 범위 초과 조심
 */
public class FirstBadVersion {
    public int firstBadVersion(int n) {
        Long start = 0L;
        Long end = Long.valueOf(n);
        Long mid = 0L;
        int answer = Integer.MAX_VALUE;

        while (start <= end) {
          mid = ((start + end) / 2L);

          if (isBadVersion(mid.intValue())) {
            answer = Math.min(answer, mid.intValue());
            end = mid - 1;
            continue;
          }

          if (!isBadVersion(mid.intValue())) {
            start = mid + 1;
          }
        }

        return answer;
    }
}
