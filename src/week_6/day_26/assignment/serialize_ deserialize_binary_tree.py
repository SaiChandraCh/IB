# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                else:
                    stack.append(None)
                    res.append(None)

                if curr.left:
                    stack.append(curr.left)
                else:
                    stack.append(None)
                    res.append(None)
            else:
                if len(stack) == 0:
                    return res

    index = 0
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if self.index >= len(data) or data[self.index] == None:
            self.index += 1
            return
        root = TreeNode(data[self.index])
        self.index += 1
        root.left = self.deserialize(self, data)
        root.right = self.deserialize(self, data)
        return root


if __name__ == '__main__':
    root = TreeNode(-1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    data = Codec.serialize(Codec,root)
    root = Codec.deserialize(Codec,data)
    print(root)
# py vs other
    # preprocessor
    # statically typed
    # static programming language
    # memory allocation
    # platform dependent
    # call by value and call by reference compared with other lang and py
    #