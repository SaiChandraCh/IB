import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        min = max(A)
        length = len(A)
        for i in range(1, length):
            for j in range(i,length):
                min = A[i - 1] ^ A[j] if A[i - 1] ^ A[j] < min else min
        return min

if __name__ == '__main__':
    print(Solution.findMinXor(Solution,[0,2,5,7]))