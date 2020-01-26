class Solution:
    # @param A : integer
    # @return an integer
    count = None
    def __init__(self):
        self.count = None
    def solve(self, A):
        if A == 0:
            return 0
        Solution.count = [None for _ in range(A+1)]
        Solution.count[1] = 1
        Solution.count[2] = 2
        for i in range(3,A+1):
            Solution.count[i] = Solution.count[i-1] + Solution.count[i-2]
        return (Solution.count[A])%((10**9)+7)

    def util(self, A):
        if not Solution.count[A]:
            vertical = Solution.util(Solution, A - 1)
            horizontal = Solution.util(Solution, A - 2)
            Solution.count[A] = horizontal + vertical
        return (Solution.count[A])%((10**9)+7)

if __name__ == '__main__':
    print(Solution.solve(Solution, 4))