class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix_sum = 0
        map = {0,1}
        for i in A:
            prefix_sum += i
            if map[prefix_sum]:
                return 1
            map[prefix_sum] = 1
        return 0

if __name__ == '__main__':
    Solution.solve(Solution,[5, 17, -22, 11])