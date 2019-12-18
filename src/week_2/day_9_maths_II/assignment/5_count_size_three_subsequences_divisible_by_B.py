class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        remainder_map = {i:0 for i in range(B)}
        for i in A:
            remainder_map[i % B] += 1
        ans = 0
        for i in range(B):
            for j in range(i,B):
                r1 = (i+j)%B
                r2 = 0 if r1 == 0 else B-r1
                if r2<j:
                    continue
                if (r1+r2)%B == 0:
                    if i == j == r2:
                        ans += remainder_map[i]*(remainder_map[i]-1)*(remainder_map[i]-2) // 6
                    elif i != j != r2:
                        ans += remainder_map[i]*remainder_map[j]*remainder_map[r2]
                    else:
                        if i == j:
                            ans += (remainder_map[i] * (remainder_map[i] - 1)//2) * remainder_map[r2]
                        elif i == r2:
                            ans += (remainder_map[i] * (remainder_map[i] - 1)//2) * remainder_map[j]
                        elif j == r2:
                            ans += (remainder_map[j] * (remainder_map[j] - 1)//2) * remainder_map[i]
        return ans

if __name__ == '__main__':
    # A = [6, 1, 1, 4, 1, 5, 3]
    # B = 2
    A = [10, 5, 10, 9, 5, 7]
    B = 3
    print(Solution.solve(Solution,A,B))
