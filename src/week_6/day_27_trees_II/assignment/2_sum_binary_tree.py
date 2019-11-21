class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    is_sum_tree = True
    def __init__(self):
       Solution.is_sum_tree = True
    def solve(self, A):
        if not A:
            return True
        Solution.util(Solution,A)
        if Solution.is_sum_tree:
            return 1
        return 0

    def util(self,root):
        if not root:
            return 0
        left_sum = Solution.util(Solution, root.left)
        right_sum = Solution.util(Solution, root.right)
        print(left_sum,right_sum,root.val)
        if root.left or root.right:
            if root.val != left_sum + right_sum:
                Solution.is_sum_tree = False
        return left_sum + right_sum + root.val

if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)

    root = TreeNode(10)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(2)
    root.right = TreeNode(2)
    print(Solution.solve(Solution,root))