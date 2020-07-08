def postorderTraversal(self, root):
    answer=[]
    return self.recursive(root, answer)

def recursive(self, root, answer):
    if root:
        self.recursive(root.left, answer)
        self.recursive(root.right, answer)
        answer.append(root.val)

    return answer

def iterative(self, root, answer):
    stack=[root]

    while stack:
        node=stack.pop()
        if node:
            answer.append(node.val)
            stack.append(root.left)
            stack.append(root.right)
    # reverse
    return answer[::-1]
