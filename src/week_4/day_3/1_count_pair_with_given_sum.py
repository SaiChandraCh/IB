class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count, i, j = 0, 0, len(A)-1
        while j>i:
            if A[i]+A[j]==B:
                count += 1
                i += 1
                j -= 1
            elif A[i]+A[j] > B:
                j -= 1
            elif A[i]+A[j] < B:
                i += 1
        return count

if __name__ == '__main__':
    print(Solution.solve(Solution, A = [1, 2, 3, 4, 5, 6],B = 6))
                         # ,[5, 10, 20, 100, 105],B = 110))