class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        c = n-1
        for i in range(n-1):
            j = 0
            while j < c:
                prev = A[i][i+j]
                print(i,i + j," <= ",n-1-i-j,i)
                A[i][i + j] = A[n-1-i-j][i]

                # temp = A[i+j][n-1-j]
                prev,A[i+j][n-1-i] = A[i+j][n-1-i],prev
                # prev = temp
                print(i+j,n-1-i," <= ",i,i + j)

                # temp = A[n-1-i][n-1-i-j]
                prev,A[n-1-i][n-1-i-j] = A[n-1-i][n-1-i-j],prev
                # prev = temp
                print(n-1-i,n-1-i-j," <= ",i+j,n-1-i)

                A[n-1-i-j][i] = prev
                print(n-1-i-j,i ," <= ",n-1-i,n-1-i-j)
                print("-------------------------------------------------------")
                j += 1
            c = c//2
        return A

if __name__ == '__main__':
    print(Solution.rotate(Solution,
                    # [[1,2],[3,4]]))
    # [
    #     [31, 32, 228, 333],
    #     [79, 197, 241, 246],
    #     [77, 84, 126, 337],
    #     [110, 291, 356, 371]
    # ]))
                          [
                              [27, 35, 36, 47, 94, 133],
                              [46, 72, 77, 95, 144, 149],
                              [13, 14, 80, 83, 121, 157],
                              [11, 38, 45, 84, 105, 132],
                              [23, 27, 42, 118, 120, 139],
                              [22, 27, 49, 85, 103, 167]
                          ]))
    #                 [[1, 2, 3],[4, 5, 6], [7, 8, 9]]))
    #                       [[1, 2, 3,4], [5, 6, 7, 8],[9,10,11,12],[13,14,15,16]]))