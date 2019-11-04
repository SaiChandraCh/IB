class Solution:
    count = 0
    no_of_ways_to_top = {}
    def __init__(self):
        Solution.count = 0
        Solution.no_of_ways_to_top = {}

    def climbStairs(self, n: int) -> int:
        return Solution.util(self, n, n)

    def util(self, total_steps, rem_steps):
        if rem_steps in Solution.no_of_ways_to_top:
            return Solution.no_of_ways_to_top[rem_steps]
        if rem_steps > -1:
            if rem_steps == 0:
                Solution.count += 1
                return Solution.count
            Solution.no_of_ways_to_top[rem_steps] = Solution.climbStairs(total_steps, rem_steps - 1)
            Solution.no_of_ways_to_top[rem_steps] = Solution.climbStairs(total_steps, rem_steps - 2)
            return Solution.no_of_ways_to_top[total_steps]

if __name__ == '__main__':
    print(Solution.climbStairs(Solution,5))