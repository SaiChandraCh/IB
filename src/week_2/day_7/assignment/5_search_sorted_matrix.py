class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A[0])
        temp = 0
        rows = []
        for row in A:
            if B >= row[0] and B <= row[n-1]:
                rows.append(temp)
            temp += 1
        for i in rows:
            for j in range(n):
                if A[i][j] == B:
                    return (i+1)*1009+(j+1)

        return -1

if __name__ == '__main__':
    print(Solution.solve(Solution,A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]],B = 2))