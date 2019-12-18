class Solution:
    # @param A : integer
    # @return an integer
    count = 0
    def __init__(self):
        self.count = 0

    def solve(self, A):
        Solution.util(Solution,A, 2, 1 )
        return self.count

    def util(self,A,i,j):
        if i == j == A:
            self.count += 1
            return
        if i < j:
            return
        if i<=A and j+1 <=A:
            Solution.util(Solution,A, i, j+1 ) # right
        if i+1<=A and j<=A:
            Solution.util(Solution,A, i+1, j ) # down

if __name__ == '__main__':
    print(Solution.solve(Solution,17))