# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    def buildTree(self, A, B):#A -> inorder, B -> postorder
        in_index = {}
        for index, val in enumerate(A):
            in_index[index] = val
        n = len(B)
        Solution.util(Solution, A, B, 0, n-1, in_index, [n-1])

    def util(self, inorder, postorder, start, end, inIndex, pIndex):
        if start > end:
            return
        node = postorder[pIndex[0]]
        pIndex[0] -= 1

        if start == end:
            return node

        

if __name__ == '__main__':
    Solution.buildTree(Solution,
                       [9,3,15,20,7],[9,15,7,20,3])
                       # [4,8,2,5,1,6,10,9,3,7],[8,4,5,2,10,9,6,7,3,1])
