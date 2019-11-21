class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count, i, j = 0, 0, len(A)-1
        while j>-1 and i<len(A):
            if A[i]*A[j]<B:
                if j>i:
                    count += j-i+1
                elif i>j:
                    count += i-j+1
                else:
                    count += 1
                print(A[i],A[j],count)
                i += 1
            else:
                j -= 1
        # count *= 2
        # for i in A:
        #     if i*i < B:
        #         count += 1
        #     else:
        #         break
        return count

if __name__ == '__main__':
    print(Solution.solve(Solution,
                         # A = [2,3,5], B = 15))#6
    A = [5, 10, 20, 100, 105],B = 110))#6
    #                      [1, 2, 3, 4, 5],5))#5
    # A = [ 10, 33, 40 ],B = 55))
    #                      A= [17, 18, 37, 68, 72, 74, 83, 109, 120, 133, 138, 141, 155, 161, 163, 164, 170, 172, 175,
    #                          192, 194, 211, 230, 231, 244, 252, 259, 264, 279, 282, 286, 290, 294, 310, 321, 325, 341,
    #                          342, 351, 359, 363, 364, 371, 397, 405, 415, 420, 426, 444, 465, 474, 493],
    # B= 777))#8