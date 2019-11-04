# class Solution:
#     # @param A : integer
#     # @return a list of integers
#     res = []
#     def __init__(self):
#         Solution.res = []
#
#     def grayCode(self, A):
#         Solution.util(Solution,A,0,0,"")
#         return Solution.res
#
#     def util(self,A,val,decimal_position,code):
#         if A == 0:
#             print(code)
#             Solution.res.append(val)
#             return
#         Solution.util(Solution,A-1,2*val,decimal_position+1,code+"0")
#         Solution.util(Solution,A-1,2*val+1,decimal_position+1,code+"1")
#
# if __name__ == '__main__':
#     Solution.grayCode(Solution,3)
#     print(Solution.res)

def grayCodeUtil(res, n, num):
    # base case when we run out bits to process
    # we simply include it in gray code sequence.
    if (n == 0):
        res.append(num[0])
        return

    # ignore the bit.
    grayCodeUtil(res, n - 1, num)
    num[0] = num[0] ^ (1 << (n - 1))
    grayCodeUtil(res, n - 1, num)


# returns the vector containing the gray
# code sequence of n bits.
def grayCodes(n):
    res = []

    # num is passed by reference to keep
    # track of current code.
    num = [0]
    grayCodeUtil(res, n, num)
    return res


# Driver Code
n = 3
code = grayCodes(n)
for i in range(len(code)):
    print(code[i])