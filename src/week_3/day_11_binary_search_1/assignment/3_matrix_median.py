class Solution:
	# @param A : list of list of integers
	# @return an integer
    def findMedian(self, A):
        m,n = len(A), len(A[0]) if A[0] else 0
        if m*n == 0:
            return 0
        if m == 1:
            if n % 2 == 0:
                return A[0][n//2]
            else:
                return (A[0][n//2] + A[0][n//2-1])//2
        median_index = (m*n)//2
        min, max = 0, A[m-1][n-1]
        while min < max:
            mid = (max-min)//2 + min


if __name__ == '__main__':
    A = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
    A = [[1, 3, 5],[2, 6, 8],[3, 6, 8]]
    Solution.findMedian(Solution,A)


