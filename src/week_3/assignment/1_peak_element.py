class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        length = len(A)
        for i in range(length):
            if (i > 1 and i<length-1 and A[i]>=A[i-1] and A[i]>=A[i+1]) or (i == length-1 and A[i] >= A[i-1]) or (i == 0 and i<length-1 and A[i] >= A[i+1]):
                return A[i]