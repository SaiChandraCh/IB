class Solution:
	# @param A : list of integers
	# @return an integer
    def largestRectangleArea(self, A):
        stack = []
        max_area = 0
        i = 0
        while i < len(A):
            if len(stack) == 0 or A[stack[-1]] < A[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if len(stack) == 0:
                    max_area = max(max_area,A[top] * i)
                elif len(stack)>0:
                    max_area = max(max_area, A[top] * (i-stack[-1]-1))

        while len(stack) > 0:
            top = stack.pop()
            if len(stack) == 0:
                max_area = max(max_area, A[top] * i)
            else:
                max_area = max(max_area, A[top] * (i - stack[-1] - 1))
        return max_area

if __name__ == '__main__':
    A = [5, 1, 1]
    print(Solution.largestRectangleArea(Solution,A))