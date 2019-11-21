class TrieNode:
    def __init__(self):
        self.child = {}
        self.freq = 1
class Solution:
	# @param A : list of strings
	# @return a list of strings
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        temp = self.root
        for char in string:
            if char not in temp.child:
                temp.child[char] = TrieNode()
            else:
                temp.child[char].freq += 1
            temp = temp.child[char]

    def search(self, root, prefix, result):
        pass
    def prefix(self, A):
        sol = Solution()
        for i in A:
            sol.insert(i)
        result = []
        # for child in sol.root.child:
            # sol.search(child, sol.root.child)

if __name__ == '__main__':
    A = ["zebra","dog","duck","dove"]
    Solution.prefix(Solution, A)

