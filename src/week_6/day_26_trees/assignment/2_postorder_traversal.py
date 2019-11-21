# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        stack = []
        res = []
        curr = A
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if not stack.__len__():
                    break
                temp = stack[stack.__len__()-1]
                if temp.right:
                    curr = temp.right
                else:
                    temp = stack.pop()
                    res.append(temp.val)
                    if stack.__len__() <= 0:
                        break
                    top = stack[stack.__len__()-1]
                    while stack.__len__() > -1 and top.right == temp:
                            temp = stack.pop()
                            res.append(temp.val)
                            if stack.__len__() <= 0:
                                break
                            top = stack[stack.__len__() - 1]
        return res

if __name__ == '__main__':
    # A = TreeNode(1)
    # temp = A
    # temp.left = TreeNode(2)
    # temp.right = TreeNode(3)
    # temp = A.left
    # temp.left = TreeNode(4)
    # temp.right = TreeNode(5)
    # temp = A.left.left
    # temp.right = TreeNode(12)
    # temp = A.left.right
    # temp.left = TreeNode(15)
    # temp.right = TreeNode(7)
    # temp = A.right
    # temp.left = TreeNode(9)
    # temp.right = TreeNode(20)
    A = TreeNode(1)
    temp = A
    temp.left = TreeNode(2)
    temp.right = TreeNode(3)
    temp = A.right
    temp.left = TreeNode(4)
    temp = A.right.left
    temp.right = TreeNode(5)
    print(Solution.postorderTraversal(Solution,A))