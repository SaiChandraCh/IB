class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        toggle_count = 0
        i = 0
        while i < len(A):
            if A[i] == '0':
                j = 0
                while j < B and i + B <= len(A):
                    A = A[:i+j]+'1'+A[i+j+1:] if A[i+j] == '0' else A[:i+j]+'0'+A[i+j+1:]
                    j += 1
                print(A)
                toggle_count += 1
            i += 1
        for i in A:
            if i == '0':
                return -1
        return toggle_count

if __name__ == '__main__':
    A = '01010'
    B = 4
    print(Solution.solve(Solution, A, B))