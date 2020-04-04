
public class TargetNumber {
    static int answer=0;
	
    public static int solution(int[] numbers, int target) {
        
        dfs(0,0,numbers,target);
        
        return answer;
    }
    
    public static void dfs(int depth, int sum, int[] numbers, int target)
    {
    	if(depth==numbers.length)
    	{
    		if(sum==target)
    			answer++;
    		return;
    	}
    	else
    	{
    		dfs(depth+1, numbers[depth]+sum, numbers, target);
    		dfs(depth+1, -numbers[depth]+sum, numbers, target);
    	}
    }
}