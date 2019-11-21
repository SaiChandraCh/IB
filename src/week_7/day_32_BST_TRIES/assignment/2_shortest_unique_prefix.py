class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.freq = 1

class Solution:
#     # @param A : list of strings
#     # @return a list of strings
    root = None
    def __init__(self):
        self.root = TrieNode()

    def get_index(self,char):
        return ord(char)-97

    def insert(self, string):
        temp = self.root
        for char in string:
            index = self.get_index(char)
            if not temp.child[index]:
                temp.child[index] = TrieNode()
            else:
                temp.child[index].freq += 1
            temp = temp.child[index]

    def search(self, root, string, index, result, substr):
        if not root:
            return substr
        if root.freq == 1:
            result.append(substr)
            return

        for i in range(26):
            if root.child[i] and chr(97+i) == string[index]:
                return self.search(root.child[i], string, index+1, result, substr+chr(97+i))

    def prefix(self, A):
        # INSERT VALUES IN TRIE
        sol = Solution()
        for i in A:
            sol.insert(i)
        result = []

        for string in A:
            if sol.root.child[ord(string[0])-97]:
                sol.search(sol.root.child[ord(string[0])-97], string, 1, result, ''+string[0])
        return result

if __name__ == '__main__':
    A = ["zebra","dog","duck","dove","yacht"]
    Solution.prefix(Solution, A)