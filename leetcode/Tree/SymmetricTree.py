def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
        
    left=self.left_search(root.left, [])
    right=self.right_search(root.right, [])

    return True if left==right else False

def right_search(self, root, arr):
    if root:
        arr.append(root.val)

        self.right_search(root.right, arr) if root.right else arr.append(0)
        self.right_search(root.left, arr) if root.left else arr.append(0)
    return arr

def left_search(self, root, arr):
    if root:
        arr.append(root.val)

        self.left_search(root.left, arr) if root.left else arr.append(0)
        self.left_search(root.right, arr) if root.right else arr.append(0)
    return arr