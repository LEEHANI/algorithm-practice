def inorderTraversal(self, root):
    answer=[]
    return self.recursive(root,answer)

def iterative(self, root, answer):
    stack=[]

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            answer.append(tmpNode.val)
            root = tmpNode.right
        
    return answer

def recursive(self, root, answer):
    if root:
        self.recursive(root.left, answer)
        answer.append(root.val)
        self.recursive(root.right, answer)

    return answer