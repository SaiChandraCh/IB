class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    b_found, c_found = False, False

    def __init__(self):
        Solution.b_found = False
        Solution.c_found = False

    def lca(self, A, B, C):
        root = Solution.util(Solution, A, B, C)
        if (Solution.b_found and Solution.c_found) or (Solution.c_found and Solution.check(Solution, root, B)) or (
                Solution.b_found and Solution.check(Solution, root, C)):
            return root.val
        return -1

    def check(self, root, val):
        que = [root]
        while que:
            curr = que.pop(0)
            if curr.val == val:
                return True
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        return False

    def util(self, A, B, C):
        if not A:
            return None
        if A.val == B:
            Solution.b_found = True
            return A
        if A.val == C:
            Solution.c_found = True
            return A
        left = Solution.util(Solution, A.left, B, C)
        right = Solution.util(Solution, A.right, B, C)
        if left and right:
            return A
        return left if left else right

if __name__ == '__main__':
    root = TreeNode(0)
    # root.left = TreeNode(2)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(3)
    # root.left.left.left = TreeNode(4)
    # root.left.left.right = TreeNode(5)
    # root.left.left.left.right = TreeNode(7)
    # root.left.left.left.right.left = TreeNode(10)
    # root.left.left.left.right.right = TreeNode(8)
    # root.left.left.right.left = TreeNode(6)
    # root.left.left.right.left.left = TreeNode(11)
    # root.left.left.right.left.right = TreeNode(9)

    print(Solution.lca(Solution,root,4, 7))
