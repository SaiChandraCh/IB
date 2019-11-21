class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        i, j = 0, 0
        while i < len(A[0]) and j < len(B):
            if A[0][i] == B[j]:
                while j+1 < len(B) and B[j] == B[j+1]:
                    j += 1
                j += 1
                i += 1
            else:
                return 0
        print(i,j,len(A[0]),len(B))
        if i == len(A[0]) and j == len(B):
            return 1
        return 0

if __name__ == '__main__':
    # A = "HIRED",
    # B = "HHHIIIRRRRREEEEEDDDDD"
    A = "HIRE",
    B = "HIRE"
    print(Solution.solve(Solution,A,B))