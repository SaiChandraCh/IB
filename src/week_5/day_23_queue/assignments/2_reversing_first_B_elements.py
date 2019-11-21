class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        i = 0
        while B-i-1 > i:
            A[i], A[B-i-1] = A[B-i-1],A[i]
            i += 1
        return A

if __name__ == '__main__':
    # A = [1, 2, 3, 4, 5, 6]
    # B = 2
    A = [ 43, 35, 25, 5, 34, 5, 8, 7 ] # 5 34 5 25 35 43 8 7
    B = 6
    print(Solution.solve(Solution,A,B))