# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        stack1 = [A]
        stack2 = []
        result = []
        while stack1 or stack2:
            temp = []
            while stack1:
                curr = stack1.pop()
                temp.append(curr)
                if curr.left:
                    stack2.append(curr.left)
                if curr.right:
                    stack2.append(curr.right)
            result.append(temp)
            temp = []
            while stack2:
                curr = stack2.pop()
                temp.append(curr)
                if curr.right:
                    stack1.append(curr.right)
                if curr.left:
                    stack1.append(curr.left)
            result.append(temp)