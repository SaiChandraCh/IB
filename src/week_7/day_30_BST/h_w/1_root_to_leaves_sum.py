class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    sum = 0

    def __init__(self):
        Solution.sum = 0

    def sumNumbers(self, A):
        Solution.util(self,A,"")
        return Solution.sum

    def util(self, root, sum):
        if not root:
            return
        if not root.left and not root.right:
            Solution.sum += int(sum+str(root.val))
            return
        Solution.util(Solution, root.left, sum+str(root.val))
        Solution.util(Solution, root.right, sum+str(root.val))
        return sum

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(Solution.sumNumbers(Solution,root))