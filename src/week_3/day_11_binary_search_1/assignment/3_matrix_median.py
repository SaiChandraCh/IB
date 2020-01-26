from bisect import bisect_right as upper_bound

MAX = 100;


# Function to find median in the matrix
def binaryMedian(m, r, d):
    mi = m[0][0]
    mx = 0
    for i in range(r):
        if m[i][0] < mi:
            mi = m[i][0]
        if m[i][d - 1] > mx:
            mx = m[i][d - 1]

    desired = (r * d + 1) // 2

    while (mi < mx):
        mid = mi + (mx - mi) // 2
        place = [0];

        # Find count of elements smaller than mid
        for i in range(r):
            j = upper_bound(m[i], mid)
            place[0] = place[0] + j
        if place[0] < desired:
            mi = mid + 1
        else:
            mx = mid
    print("Median is", mi)
    return


# Driver code
r, d = 3, 3

m = [[1, 3, 4], [2, 6, 9], [3, 6, 9]]
binaryMedian(m, r, d)

# class Solution:
# 	# @param A : list of list of integers
# 	# @return an integer
#     def findMedian(self, A):
#         m,n = len(A), len(A[0]) if A[0] else 0
#         if m*n == 0:
#             return 0
#         if m == 1:
#             if n % 2 == 0:
#                 return A[0][n//2]
#             else:
#                 return (A[0][n//2] + A[0][n//2-1])//2
#         median_index = (m*n)//2
#         min, max = 0, A[m-1][n-1]
#         while min < max:
#             mid = (max-min)//2 + min
#
#
# if __name__ == '__main__':
#     A = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
#     A = [[1, 3, 5],[2, 6, 8],[3, 6, 8]]
#     Solution.findMedian(Solution,A)
#
#
