class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isValidBST(self, A):
        return Solution.util(Solution,A, -4294967296, 4294967296)

    def util(self, root, min, max):
        if not root:
            return True
        if root.val > max:
            return False
        if root.val < min:
            return False
        if not Solution.util(Solution, root.left, min, root.val-1) or not Solution.util(Solution, root.right, root.val+1, max):
            return False
        return True

if __name__ == '__main__':
    root = TreeNode(18)
    root.left = TreeNode(9)
    root.right = TreeNode(25)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(18)
    print(Solution.isValidBST(Solution,root))

