Dynamic Programming
===
DP는 큰 문제를 여러 개의 작은 문제로 나눠 푸는 방법을 말한다. 작은 문제를 풀 때 같은 문제들이 반복해서 나오는데, 같은 문제를 반복해서 계산하지 않도록 값을 저장해놨다가 재사용 하는 메모이제이션 기법을 사용한다. 

Top-Down, Bottom-Up의 두가지 구현 방식이 존재한다.    
  * Top-Down: 여러 개의 하위 문제로 나눠 푼 다음, 그것을 결합하여 최적해를 찾는다.   
  * Bottom-Up 하위 문제들로 상위 문제의 최적해를 구한다.    
<br/>  
<br/>
### 소스코드    
대표적인 예로 피보나치 수열이 있다.

```
//Top-Down
fibonacci(int n)
{
	dp[0] = 1
	dp[1] = 1
	
	if(dp[n] != 0)
	{
		return dp[n]
	}
	else
	{
		dp[n] = fibonacci(n-2) + fibonacci(n-1)
			
		return dp[n]
	}
}
```
```
// Bottom-Up
fibonacci(int n)
{
	dp[0] = 1
	dp[1] = 1
	
	for(int i = 2 ; i <= n ; i ++)
	{
		dp[i] = dp[i-1] + dp[i-2]
	}
	
	return dp[n]
}
```
