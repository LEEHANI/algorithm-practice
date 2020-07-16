def maxDepth(self, root):
    return self.search(root, 0, 0)

def search(self, root, depth):
    if root:
        return 1+max(self.search(root.left, depth+1), self.search(root.right, depth+1))
    else:
        return 0