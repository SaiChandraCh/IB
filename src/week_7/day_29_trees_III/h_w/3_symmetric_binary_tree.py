class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isSymmetric(self, A):
        return Solution.isMirror(Solution,A.left,A.right)

    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return 1
        if not root1 or not root2 or (root1 and root2 and root1.val == root2.val):
            return 0
        if root1 and root2 and root2.val == root1.val:
            return Solution.isMirror(self, root1.left, root2.right) and Solution.isMirror(self, root1.right, root2.left)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)

    print(Solution.isSymmetric(Solution,root))

    # que = [A]
    # while que:
    #     curr = que.pop(0)
    #     print(curr.val)
    #     if curr.left:
    #         que.append(curr.left)
    #     if curr.right:
    #         que.append(curr.right)