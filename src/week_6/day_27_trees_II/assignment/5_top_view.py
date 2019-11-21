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
        result = {0:root.val}
        Solution.pre_util(Solution, root.left, -1, result, 0)
        print(result)
        Solution.post_util(Solution, root.right, 1, result, 0)

        return [result[key] for key in result]

    def pre_util(self, root, level, result, min):
        if not root:
            return
        if level < min and level not in result:
            result[level] = root.val
            min = level
        Solution.pre_util(Solution, root.left, level-1, result, min)
        Solution.pre_util(Solution, root.right, level+1, result, min)


    def post_util(self, root, level, result, max):
        if not root:
            return
        if level > max and level not in result:
            result[level] = root.val
            max = level
        Solution.post_util(Solution, root.right, level+1, result, max)
        Solution.post_util(Solution, root.left, level-1, result, max)

if __name__ == '__main__':
    A = [7722, 9970, 4002, 7668, 7935, 1936, 8299, 9867, 4806, 5189, 3778, 8567, 5263, 189, 8603, 8477, 6760, 9299, 9796, 3139, 1319, 4025, 6778, 4701, 9212, 3082, 2462, 3251, 1148, 4323, 7475, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    # 4002 7475 8299 8603 ---- 7722 9970 7668 9867 8477
    # A = [18 ,14 ,20 ,10 ,27 ,25 ,None ,None ,None ,None ,None ,None ,None]
    root = TreeNode(A[0])
    que = [root]
    i = 0
    while 2*i+2 < len(A):
        curr = que.pop(0)
        if A[2*i+1]:
            curr.left = TreeNode(A[2*i+1])
        if A[2*i+2]:
            curr.right = TreeNode(A[2*i+2])
        que.append(curr.left)
        que.append(curr.right)
        i += 1
    print(Solution.solve(Solution,root))