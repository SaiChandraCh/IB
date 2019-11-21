class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        pair = []
        for i in range(len(A)):
            pair.append([B[i],A[i]])
        pair.sort()
        no_of_tasks = 1
        prev_task_end_time = pair[0][0]
        for i in range(1,len(A)):
            if prev_task_end_time <= pair[i][1]:
                no_of_tasks += 1
                prev_task_end_time = pair[i][0]
        return no_of_tasks

if __name__ == '__main__':
    # A = [8, 1, 3, 0, 5, 5] # start time
    # B = [9, 2, 4, 6, 7, 9] # finish time
    A = [2, 30, 4, 13, 1, 6, 3, 13]
    B = [40, 49, 11, 30, 37, 23, 30, 37]
    print(Solution.solve(Solution, A, B))