def preorderTraversal(self, root):
    answer=[]
    return self.iterative(root, answer)

def iterative(self, root, answer):
    stack=[root]

    while stack:
        node=stack.pop()
        if node:
            answer.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

    return answer

def recursive(self, root, answer):
    if root:
        answer.append(root.val)
        self.preorderTraversalRecursive(root.left, answer)
        self.preorderTraversalRecursive(root.right, answer)
    
    return answer