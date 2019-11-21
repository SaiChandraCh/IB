class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class binary_tree_util:
    def build(A):
        root = TreeNode(A[0])
        que = [root]
        i = 0
        while 2*i+2 < len(A):
            curr = que.pop(0)
            if A[2*i+1]:
                curr.left = TreeNode(A[2*i+1])
                que.append(curr.left)
            if A[2*i+2]:
                curr.right = TreeNode(A[2*i+2])
                que.append(curr.right)
            i += 1
        return root