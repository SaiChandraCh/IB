class Solution:
    def canJump(self, A):
        if len(A) == 1:
            return True
        visited = {}
        return Solution.util(self, 0, A[0], A, visited)

    def util(self, curr, max_steps_from_curr, A, visited):
        if curr in visited:
            return visited[curr]
        if max_steps_from_curr == 0:
            return False
        if curr+max_steps_from_curr >= len(A) - 1:
            return True
        for i in range(max_steps_from_curr, 0, -1):
            if curr+i >= len(A):
                return True
            visited[A[curr + i]] = Solution.util(Solution, curr + i, A[curr + i], A, visited)
            if visited[A[curr + i]]:
                return True
        return False

if __name__ == '__main__':
    A = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print(Solution.canJump(Solution, A))