def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    return self.search(root, sum, root.val)

def search(self, root, sum, total):
    if root:
        if sum==root.val+total and not root.left and not root.right:
            return True

        # if self.search(root.left, sum, root.val+total):
        #     return True
        # if self.search(root.right, sum, root.val+total):
        #     return True
        return self.search(root.left, sum, root.val+total) or self.search(root.right, sum, root.val+total)

    return False  