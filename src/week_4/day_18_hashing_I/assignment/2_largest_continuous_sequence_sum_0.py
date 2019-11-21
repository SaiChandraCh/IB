class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        prefix_sum = 0
        map = {}
        largest, result = [], 0
        length = len(A)
        map[0] = 0
        for i in range(length):
            prefix_sum += A[i]
            if prefix_sum in map:
                if i+1 - map[prefix_sum] > len(largest):
                    if prefix_sum == 0:
                        largest = A[:i+1]
                    else:
                        largest = A[map.get(prefix_sum):i+1]
                continue
            map[prefix_sum] = i+1
        return largest

if __name__ == '__main__':
    print(Solution.lszero(Solution,
                          # [-16, -10, -7, -11, 16, -15, 2, 28, -27, 19, -20, -22, -22, 21, -21, 18, -20, 24, 24, -12,-27, 2, -13, 3, 1, -18, 10, 20, -29, -4]
                          # [ 1, 2, -2, 4, -4 ]
                          # [1, 2, -3, 3]
                          [1, 2, -1, 1, 3, -1, 1, 4] # [-1,1]
                          ))