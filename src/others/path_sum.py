class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    found = False

    def hasPathSum(self, root: TreeNode, sum: int):
        if root is None:
            return (sum == 0)
        else:
            ans = False

            # Otherwise check both subtrees
            subSum = sum - root.val

            # If we reach a leaf root and sum becomes 0, then
            # return True
            if (subSum == 0 and root.left == None and root.right == None):
                return True

            if root.left is not None:
                ans = ans or Solution.hasPathSum(Solution,root.left, subSum)
            if root.right is not None:
                ans = ans or Solution.hasPathSum(Solution,root.right, subSum)

            return ans

            #     if root:
    #         return True if Solution.hasSum(Solution, root, 0, sum) else False
    #     return False
    #
    # def hasSum(self, root, sum, required_sum):
    #     if not Solution.found and root and sum < required_sum:
    #         sum += root.val
    #         if sum == required_sum:
    #             return True
    #         Solution.found = Solution.hasSum(Solution, root.left, sum, required_sum)
    #         Solution.found = Solution.hasSum(Solution, root.right, sum, required_sum)
    #     return Solution.found

# [5,4,8,11,null,13,4,7,2,null,null,null,1]
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(Solution.hasPathSum(Solution,root,22))