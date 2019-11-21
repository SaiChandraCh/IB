class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
    def hasPathSum(self, root, B):
        if root:
            if not root.left and not root.right and root.val == B:
                return 1
            return Solution.hasPathSum(Solution, root.left, B - root.val) or Solution.hasPathSum(Solution, root.right, B - root.val)
        return 0

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    B = 22

    # root = TreeNode(1000)
    # root.left = TreeNode(2000)
    # root.left.left = TreeNode(-3001)
    # B = -1
    print(Solution.hasPathSum(Solution,root, B))