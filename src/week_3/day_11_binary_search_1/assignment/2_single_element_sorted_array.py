class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        length = len(A)
        left = 0
        right = length-1
        while left < right:
            mid = left + (right-left)//2
            if A[mid] == A[mid-1]:
                if (mid)%2 != 0:
                    left = mid+1
                else:
                    right = mid-1
            elif A[mid] == A[mid+1]:
                if mid%2 == 0:
                    left = mid+1
                else:
                    right = mid-1
            else:
                return A[mid]
        return A[left]

if __name__ == '__main__':
    print(Solution.solve(Solution,A =
    # [0,1, 1, 2, 2, 3, 3]))
    # [1, 1, 2, 2, 3]))
    [5, 11, 11, 100, 100]))