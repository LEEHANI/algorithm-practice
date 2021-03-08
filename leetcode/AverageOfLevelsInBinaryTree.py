# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # [node, depth]
        qu = [[root, 0]]        
        answer=[]
        
        cnt = 0
        val = 0
        currentDepth=0
        
        while qu:
            target = qu.pop(0)
            
            if target[1] != currentDepth:
                currentDepth=currentDepth+1
                answer.append(val/cnt)
                cnt=0
                val=0
            
            if target[0].left != None:
                qu.append([target[0].left, currentDepth+1])
            if target[0].right != None:
                qu.append([target[0].right, currentDepth+1])
                
            val=val+target[0].val
            cnt=cnt+1
            
        if cnt:
            answer.append(val/cnt)
            
        return answer
        