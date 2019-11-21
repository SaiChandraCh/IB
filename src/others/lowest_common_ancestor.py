from util.BT_deserialise import BT_deserialise
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left_lca = Solution.lowestCommonAncestor(Solution,root.left, p, q)
        right_lca = Solution.lowestCommonAncestor(Solution,root.right, p, q)
        if left_lca and right_lca:
            return root

if __name__ == '__main__':
    root = BT_deserialise.deserialize(BT_deserialise,[3,5,1,6,2,0,8,None,None,7,4])
    print(Solution.lowestCommonAncestor(Solution,root,TreeNode(5),TreeNode(1)).val)


# 61 16 23 9 -1 1 22 2 25 19 6 13 -1 24 14 -1 30 4 26 29 -1 -1 -1 -1 -1 3 -1 8 -1 -1 12 18 28 -1 10 -1 5 -1 17 11 21 7 -1 -1 -1 20 -1 -1 -1 -1 -1 15 -1 -1 -1 -1 -1 -1 -1 27 -1 -1
# 32
# 24