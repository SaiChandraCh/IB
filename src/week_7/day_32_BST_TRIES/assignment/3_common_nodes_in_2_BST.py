class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, root1, root2):
        stack1, stack2 = [],[]
        sum = 0
        while True:
            if root1:
                stack1.append(root1)
                root1 = root1.left
            elif root2:
                stack2.append(root2)
                root2 = root2.left
            elif len(stack1) != 0 and len(stack2) != 0:
                root1 = stack1[-1]
                root2 = stack2[-1]
                if root1.val == root2.val:
                    sum += root2.val
                    stack1.pop()
                    stack2.pop()
                    root1 = root1.right
                    root2 = root2.right
                elif root1.val< root2.val:
                    stack1.pop()
                    root1 = root1.right
                    root2 = None
                elif root1.val> root2.val:
                    stack2.pop()
                    root2 = root2.right
                    root1 = None
            else:
                break
        return sum
if __name__ == '__main__':
    from util.binary_tree_util import binary_tree_util
    A = [25, 18, 30, 14, 21, 28, 33, 6, 17, 20, 22, 27, 29, 31, 43, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    B = [18, 11, 24, 6, 14, 21, 28, 4, 7, 12, 16, 19, 22, 25, 31, None, 5, None, 9, None, 13, 15, 17, None, 20, None, 23, None, 26, 30, 34, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    Solution.solve(Solution,binary_tree_util.build(A),binary_tree_util.build(B))