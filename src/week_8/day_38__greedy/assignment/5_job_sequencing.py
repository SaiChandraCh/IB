class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        pair = []
        for i in range(len(A)):
            pair.append([B[i],A[i]])
        pair.sort(reverse=True)
        sum = 0
        profit = [0]*(max(A))
        for i in range(len(A)):
            j = pair[i][1]-1
            if profit[j] == 0:
                profit[j] = pair[i][0]
                sum += pair[i][0]
            else:
                while j>=0:
                    if profit[j] == 0:
                        profit[j] = pair[i][0]
                        sum += pair[i][0]
                        break
                    j -= 1
        return sum
if __name__ == '__main__':
    A = [9, 1, 9, 7, 5, 1, 9, 7, 5, 6, 5]
    B = [9, 3, 30, 43, 10, 10, 7, 18, 34, 4, 41]
    # A = [2, 1, 2, 1, 3]
    # B = [100, 19, 27, 25, 15]
    print(Solution.solve(Solution, A, B))