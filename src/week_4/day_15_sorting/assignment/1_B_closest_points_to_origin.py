class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers

    def __init__(self):
        pass

    def solve(self, A, B):
        A.sort(key=lambda x : int((x[0]**2+x[1]**2)**1/2))
        return A[:B]

if __name__ == '__main__':
    print(Solution.solve(Solution,A = [[26, 41],[40, 47],[47, 7],[50, 34],[18, 28]],B = 5))
