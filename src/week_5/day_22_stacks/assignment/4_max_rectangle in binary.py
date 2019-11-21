class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        for col in range(cols):
            temp = 0
            for row in range(rows):
                if A[row][col] == 0:
                    temp = 0
                else:
                    temp += A[row][col]
                    A[row][col] = temp

        max_area = 0
        for row in A:
            stack = []
            i = 0
            while i < cols:
                if len(stack) == 0 or row[stack[-1]] < row[i]:
                    stack.append(i)
                    i += 1
                else:
                    top = stack.pop()
                    if len(stack) == 0:
                        max_area = max(max_area, row[top] * i)
                    else:
                        max_area = max(max_area, row[top] * (i - stack[-1] - 1))

            while len(stack) > 0:
                top = stack.pop()
                if len(stack) == 0:
                    max_area = max(max_area, row[top] * i)
                else:
                    max_area = max(max_area, row[top] * (i - stack[-1] - 1))
        return max_area

if __name__ == '__main__':
    A = [[0, 0, 1],  [0, 1, 1],  [1, 1, 1]]#,  [1, 0, 0],  [1, 0, 0],  [1, 1, 1],  [0, 1, 0]]
    print(Solution.solve(Solution,A))