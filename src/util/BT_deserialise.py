class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BT_deserialise:
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

