class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        lamp_loc_map, x_map, y_map = {}, {}, {}
        D = []
        for i in B:
            lamp_loc_map[i[0]*A+i[1]] = True
            if i[0] in x_map:
                x_map[i[0]] += 1
            else:
                x_map[i[0]] = 1

            if i[1] in y_map:
                y_map[i[1]] += 1
            else:
                y_map[i[1]] = 1

        for i in C:
            # if i[0] in x_map
            pass
if __name__ == '__main__':
    A = 5,
    B = [[0, 4], [4, 4]],
    C = [[1, 1], [1, 0]]
    Solution.solve(Solution,A,B,C)