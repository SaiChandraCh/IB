class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        open_doors = 1
        for i in range(2,A+1):
            root = int(i ** (0.5))
            if root*root == i:
                open_doors += 1
        return open_doors

if __name__ == '__main__':
    print(Solution.solve(Solution, 995712))