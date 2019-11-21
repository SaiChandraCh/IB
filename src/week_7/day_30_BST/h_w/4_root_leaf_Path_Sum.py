class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return a list of list of integers
    def pathSum(self, A, B):
        result = []
        Solution.util(self, A, B,[],result)
        return result
    def util(self,root,B,temp,result):
        if not root:
            return
        if not root.left and not root.right:
            if B == root.val:
                result.append(temp+[root.val])
            return
        Solution.util(self, root.left, B-root.val, temp+[root.val],result)
        Solution.util(self, root.right, B-root.val, temp+[root.val],result)
        return
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(Solution.pathSum(Solution,root,22))
