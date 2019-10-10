class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    left_max, right_min = 0,0
    def isValidBST(self, A):
        if A == None:
            return
        self.left_max = A.val
        self.right_min = A.val
        if A.left and A.left.val<A.val and self.util_left(A.left)<A.val:
            return True
        else:
            return False

        if A.right and A.right.val>A.val and self.util_right(A.right) > A.val:
            return True
        else:
            return False
    def util_left(self,root):
        if root == None:
            return 0
        if root.left.val>root.val or (root.right and root.right.val<root.val):
            return False
        self.left_max = max(self.left_max,self.util_left(self,root.left))
        return self.left_max

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)
    print(Solution.isValidBST(Solution,root))