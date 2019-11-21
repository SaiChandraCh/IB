class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    isBal = True
    def isBalanced(self, A):
        left_height = Solution.util(Solution, A.left)
        right_height = Solution.util(Solution, A.right)
        if Solution.isBal and ((left_height >= right_height and left_height - right_height < 2) or (right_height >= left_height and right_height-left_height < 2)):
            return 1
        return 0

    def util(self, root):
        if not root:
            return 0
        left_height = Solution.util(Solution, root.left)
        right_height = Solution.util(Solution, root.right)
        if not (left_height >= right_height and left_height - right_height < 2) or (right_height >= left_height and right_height-left_height < 2):
            print(False)
            Solution.isBal = False
        return 1+max(left_height, right_height)

if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.right = TreeNode(6)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(8)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right.right.right = TreeNode(4)
    print(Solution.isBalanced(Solution,root))