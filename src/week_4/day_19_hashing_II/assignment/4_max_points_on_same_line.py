class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        max_points = 0
        for i in range(len(A)):
            slope_map = {}
            vertical_point, overlapping_point, curr_max = 0, 0, 0
            for j in range(i+1,len(B)):
                y_diff = (B[j] - B[i])
                x_diff = (A[j] - A[i])
                if y_diff == x_diff == 0:
                    overlapping_point += 1
                elif x_diff != 0:
                    slope = y_diff / x_diff
                    if slope in slope_map:
                        slope_map[slope] += 1
                    else:
                        slope_map[slope] = 1
                    curr_max = max(curr_max,slope_map[slope])
                else:
                    vertical_point += 1
                temp = max(curr_max,vertical_point)
                max_points = max(temp+1+overlapping_point, max_points)
        return max_points

if __name__ == '__main__':
    print(Solution.solve(Solution,
                            # A = [6, -7, 5, 9, -9, -7],
                            # B = [7, 5, 5, 9, -8, 2]
                            # A=[-1, 0, 1, 2, 3, 3],
                            # B = [1, 0, 1, 2, 3, 4]
                            A = [2,  1, -7,   4, 1,  -2, -7, 5],
                            B = [-6, -7, 3, -10, 7, -10,  1, 2]
                            # A = [3, 1, 4, 5, 7, -9, -8, 6],
                            # B = [4, -8, -3, -2, -1, 5, 7, -4]
                   ))