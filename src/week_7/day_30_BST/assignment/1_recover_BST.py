class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers

    def recoverTree(self, A):
        min, max = -4294967296, 4294967296
        Solution.util(self, A, min, max)

    def util(self, root, min, max):
        if not root:
            return True
        if root.val > max:
            return False
        # Solution.util(self, root.left, min, root.val-1)
        if root.val < min:
            return False
        # if Solution.util(self, root.left, min, root.val-1)

