class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    distance = 0
    def __init__(self):
        Solution.distance = 0

    def solve(self, A, B, C):
        root = Solution.lca(self, A, B, C)
        distance1 = Solution.util(self,root, B, 0)
        distance2 = Solution.util(self,root, C, 0)
        return distance1+distance2

    def lca(self, root, B, C):
        if not root:
            return
        if root.val == B or root.val == C:
            return root
        left = Solution.lca(self, root.left, B, C)
        right = Solution.lca(self, root.right, B, C)
        if left and right:
            return root
        return left if left else right

    def util(self,root, val, level):
        if not root:
            return 0
        if root.val == val:
            return level
        return Solution.util(self, root.left, val, level+1) or Solution.util(self, root.right, val, level+1)

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(6)
    root.right.right = TreeNode(11)
    print(Solution.solve(Solution, root, 2, 1))