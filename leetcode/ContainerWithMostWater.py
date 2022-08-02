'''
가장 큰 네모박스를 찾으면 된다. 
한 칸씩 너비를 줄여가며 가장 네모를 찾아나가자.

너비와 높이가 큰걸 찾으면 되는데, 중요한 포인트는 물의 넓이는 막대기가 작은 쪽에 의해 결정된다는 점. 
(1, 7) 일때, 1에 의해 물의 넓이가 결정. 

양쪽에 포인터를 둬서 둘 중 작은애 포인터를 옮긴다. 
'''
class Solution:
  def maxArea(self, height) -> int:
    start=0
    end=len(height)-1
    h=0
    answer=0

    while(start<end):
      h=min(height[start], height[end])
      answer=max(answer,(end-start)*h)
      if height[start] < height[end]:
        start=start+1
      else:
        end=end-1

    return answer

  
if __name__=="__main__":
  sol1 = Solution()
  # print(sol1.maxArea([1,8,6,2,5,4,8,3,7]))
  # print(sol1.maxArea([3,9,3,4,7,2,12,6]))
  print(sol1.maxArea([1,2,4,3]))