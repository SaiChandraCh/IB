class Solution:
	# @param A : list of strings
	# @return a strings
    def longestCommonPrefix(self, A):
        length = len(A)
        res = A[0]
        for index in range(1,length):
            i = 0
            j = 0
            while i< len(res) and j < len(A[index]) and res[i] == A[index][j]:
                i +=1
                j +=1
            res = A[index][0:j]
        return res

if __name__ == '__main__':
    print(Solution.longestCommonPrefix(Solution,
                                       # ["abcdefgh", "aefghijk", "abcefgh"]))
                                       # ["abab", "ab", "abcd"]))
                                       ["abcd", "abcd", "efgh"]))