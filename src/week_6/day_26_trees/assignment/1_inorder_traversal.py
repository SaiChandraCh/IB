# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []
        res = []
        curr = A
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if not len(stack):
                    break
                else:
                    temp = stack.pop()
                    res.append(temp)
                    temp = temp.right


if __name__ == '__main__':
    A = TreeNode(1)
    temp = A
    A.right = TreeNode(2)
    temp = temp.right
    temp.left = TreeNode(2)
    print(Solution.inorderTraversal(Solution,A))
