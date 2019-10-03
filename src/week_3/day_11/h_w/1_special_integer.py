class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        length = len(A)
        start, end = 0, 0
        sum, maxLen = A[0], length
        while start <= end:
            if sum < B:

                maxLen = (end-start)+1
                if end < length-1:
                    end += 1
                sum += A[end]
            else:
                sum -= A[start]
                start += 1
        return maxLen

if __name__ == '__main__':
    print(Solution.solve(Solution,
                   A = [1, 2, 3, 4, 5],B = 10))