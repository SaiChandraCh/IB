class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        result = {1}
        i = 2
        while i <= (A**1/2):
            if A%i == 0:
                result.add(i)
                if A//i != i and i != 1:
                    result.add(A//i)
            i += 1
        return len(result)

if __name__ == '__main__':
    A = 2
    print(Solution.solve(Solution, A))