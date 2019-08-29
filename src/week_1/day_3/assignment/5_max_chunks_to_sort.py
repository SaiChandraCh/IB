class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        length = len(A)
        count = 0
        val = 0
        index = 0
        # while index < length and val < length:
        #     val += 1
        #     if val == A[index]:
        #         index += 1
        #     else:
        #         count += 1
        return count

if __name__ == '__main__':
    print(Solution.solve(Solution,[2,3, 0, 1, 4]))