class TrieNode:
    def __init__(self):
        self.child = {}
        self.isTerminal = None

class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        Solution.root = TrieNode()
        Solution.result = 0
        Solution.insert_status = 0

    def insert(self, binary_number, max_len):
        prefix = '0'*(max_len-len(binary_number))
        binary_number = prefix + binary_number
        print(binary_number)
        temp = Solution.root
        for bit in binary_number:
            if bit not in temp.child:
                temp.child[bit] = TrieNode()
            temp = temp.child[bit]

    def solve(self, A):
        sol = Solution()
        max_A = max(A)
        max_len = len(bin(max_A))-2
        for i in A:
            sol.insert(bin(i)[2:],max_len)
        print(sol.result)

if __name__ == '__main__':
    # A = [1, 2, 3, 4, 5] #7
    A = [5, 17, 100, 11] # 117
    Solution.solve(Solution,A)