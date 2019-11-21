class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        if not root:
            return
        result = []
        result.append(root.val)
        Solution.pre_util(Solution, root.left, result)
        Solution.leaf_nodes_util(Solution, root.left, result)
        Solution.leaf_nodes_util(Solution, root.right, result)
        Solution.post_util(Solution, root.right, result)
        return result

    def leaf_nodes_util(self, curr, result):
        if not curr:
            return
        self.leaf_nodes_util(self,curr.left, result)
        if not curr.left and not curr.right:
            result.append(curr.val)
        self.leaf_nodes_util(self, curr.right, result)


    def pre_util(self, root, result):
        if not root or (root and not root.left and not root.right):
            return
        result.append(root.val)
        if root.left:
            Solution.pre_util(Solution, root.left, result)
        elif root.right:
            Solution.pre_util(Solution, root.right, result)

    def post_util(self, root, result):
        if not root or (root and not root.left and not root.right):
            return
        if root.right:
            Solution.post_util(Solution, root.right, result)
        elif root.left:
            Solution.post_util(Solution, root.left, result)
        result.append(root.val)


if __name__ == '__main__':
    A = [1,2,3,4,5,6,None,None,None,7,8,9,10]
    from src.util.binary_tree_util import binary_tree_util
    print(Solution.solve(Solution,binary_tree_util.build(A)))