class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        memoize = {}
        return self.util(self, A, memoize)

    def util(self, n, memoize):
        if n in memoize:
            return memoize[n]
        if n<0:
            return 0
        if n < 2:
            return 1
        memoize[n] = self.util(self, n-1, memoize) + self.util(self, n-2, memoize)
        return memoize[n]

if __name__ == '__main__':
    print(Solution.climbStairs(Solution,2))