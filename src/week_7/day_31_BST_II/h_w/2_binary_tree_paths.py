# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        result = []
        Solution.util(self, A, [], result)
        return result

    def util(self, root, temp, result):
        if not root:
            return
        if not root.left and not root.right:
            result.append(temp+[root.val])
        Solution.util(self,root.left,temp+[root.val],result)
        Solution.util(self,root.right,temp+[root.val],result)