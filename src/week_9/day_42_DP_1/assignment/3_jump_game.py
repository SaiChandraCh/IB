class Solution:
    def jump(self, nums):
        length = len(nums)
        max_jump = nums[0]
        if length == 1:
            return 0
        visited = [0 for _ in range(length)]
        for index in range(length):
            print(visited)
            if index > max_jump:
                return -1
            max_jump = max(max_jump, index+nums[index])
            if visited[length-1] > 0:
                return visited[length-1]
            for j in range(index+nums[index], 0, -1):
                if j >= length-1:
                    return visited[index]+1
                if visited[j] != 0:
                    break
                visited[j] = visited[index] + 1
        return visited[length-1]

if __name__ == '__main__':
    # A = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    # A = [2,3,1,1,4]
    A =  [ 33, 21, 50, 0, 0, 46, 34, 3, 0, 12, 33, 0, 31, 37, 15, 17, 34, 18, 0, 4, 12, 41, 18, 35, 37, 34, 0, 47, 0, 39, 32, 49, 5, 41, 46, 26, 0, 2, 49, 35, 4, 19, 2, 27, 23, 49, 19, 38, 0, 33, 47, 1, 21, 36, 18, 33, 0, 1, 0, 39, 0, 22, 0, 9, 36, 45, 31, 4, 14, 48, 2, 33, 0, 39, 0, 37, 48, 44, 0, 11, 24, 16, 10, 23, 22, 41, 32, 14, 22, 16, 23, 38, 42, 16, 15, 0, 39, 23, 0, 42, 15, 25, 0, 41, 2, 48, 28 ]
    print(Solution.jump(Solution, A))