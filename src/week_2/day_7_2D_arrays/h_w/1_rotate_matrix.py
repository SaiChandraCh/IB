class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        n = 5
        c = n-1
        temp = 0
        for i in range(n-1):
            j = i
            while j < c:
                prev = A[j][c]
                A[j][c] = A[i][j]
                prev, A[c][c-j+temp] = A[c][c-j+temp],prev
                prev, A[c-j+temp][i] = A[c-j+temp][i],prev
                A[i][j] = prev
                j += 1
            c -= 1
            temp +=1
        return A

if __name__ == '__main__':
    print(Solution.rotate(Solution,
                    # [[1,2],[3,4]]))
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]))
    #                       [
    #                           [27, 35, 36, 47, 94, 133],
    #                           [46, 72, 77, 95, 144, 149],
    #                           [13, 14, 80, 83, 121, 157],
    #                           [11, 38, 45, 84, 105, 132],
    #                           [23, 27, 42, 118, 120, 139],
    #                           [22, 27, 49, 85, 103, 167]
    #                       ]))
    #                 [[1, 2, 3],[4, 5, 6], [7, 8, 9]]))
    #                       [[1, 2, 3,4], [5, 6, 7, 8],[9,10,11,12],[13,14,15,16]]))