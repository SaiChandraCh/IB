class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        # str = A.split(" ")
        # stack = []
        # for i in str:
        #     if i:
        #         stack.insert(0,i)
        # str = ""
        # for i in stack:
        #     str += i+" "
        #
        # return str.rstrip()

        prev = 0
        for i in A:
            print(i)

if __name__ == '__main__':
    print(Solution.solve(Solution,"the sky is       blue"))