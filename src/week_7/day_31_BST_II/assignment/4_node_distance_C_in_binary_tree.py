class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer NODE TO FOUND
    # @param C : integer DISTANCE
    # @return a list of integers
    def solve(self, A, B, c):
        parent_table = {}
        root = Solution.level_order(Solution, A, B, parent_table)
        visited = {}
        que = [root, None]
        while c>0 and que:
            curr = que.pop(0)
            if curr:
                if curr.val not in visited:
                    if curr.val in parent_table:
                        que.append(parent_table[curr.val])
                    visited[curr.val] = True
                if curr.left and curr.left.val not in visited:
                    que.append(curr.left)
                    visited[curr.left.val] = True
                if curr.right and curr.right.val not in visited:
                    que.append(curr.right)
                    visited[curr.right.val] = True
            else:
                c -= 1
                que.append(None)
        result = []
        while que:
            curr = que.pop(0)
            if curr:
                result.append(curr.val)
        return result


    def level_order(self, root, val, map):
        que = [root]
        result = None
        while que:
            curr = que.pop(0)
            if curr.val == val:
                result = curr
            if curr.left:
                que.append(curr.left)
                map[curr.left.val] = curr
            if curr.right:
                que.append(curr.right)
                map[curr.right.val] = curr
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    B = 3
    C = 3
    print(Solution.solve(Solution, root, B, C))