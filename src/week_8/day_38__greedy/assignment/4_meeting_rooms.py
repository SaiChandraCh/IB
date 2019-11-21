class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 0:
            return
        A.sort()
        rooms = [A[0][1]]
        for i in range(1,len(A)):
            j = 0
            while j < len(rooms):
                if rooms[j]<=A[i][0]:
                    rooms[j] = A[i][1]
                    break
                j += 1
            if j == len(rooms):
                rooms.append(A[i][1])
        return len(rooms)

if __name__ == '__main__':
    # A = [[1, 18],
    #      [18, 23],
    #      [15, 29],
    #      [4, 15],
    #      [2, 11],
    #      [5, 13]]
    # A = [[0, 30],
    #      [5, 10],
    #      [15, 20]]
    A = [[7, 10],
          [4, 19],
          [19, 26],
          [14, 16],
          [13, 18],
          [16, 21]]
    Solution.solve(Solution,A)
