# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        node = root

        q=[[node,0]]
        m={}
        deepest=0
        while node:
            target, dep = q.pop(0)
            deepest=dep
            if dep in m:
                m[dep]+=target.val
            else:
                m[dep]=target.val

            if target.left:
                q.append([target.left, dep+1])
            if target.right:
                q.append([target.right, dep+1])

    return m[deepest]