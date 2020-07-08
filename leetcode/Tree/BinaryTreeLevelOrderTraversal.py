def levelOrder(self, root):
    answer=[]
    return self.bfs(root, answer,0)

def bfs(self, root, answer, depth):
    if root:
        try:
            answer[depth].append(root.val)
        except IndexError as identifier:
            answer.append([root.val])

        self.bfs(root.left, answer, depth+1)
        self.bfs(root.right, answer, depth+1)
    return answer