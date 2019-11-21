class Solution:
    # @param A : list of characters
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        map = {}
        queries = []
        for i in range(len(A)):
            decimal_str = ""
            temp = int(B[i])
            while A[i] != "?" and temp > 0:
                if (temp % 10) % 2 == 0:
                    decimal_str = "0"+decimal_str
                else:
                    decimal_str = "1"+decimal_str
                temp //= 10
            if A[i] == '+':
                if decimal_str in map:
                    map[decimal_str] += 1
                    continue
                map[decimal_str] = 1
            elif A[i] == '-':
                if decimal_str in map:
                    map[decimal_str] -= 1
            else:
                print(map)
                # queries.append(map[decimal_str])
        return queries

if __name__ == '__main__':
    # A = [ "+", "+", "?", "+", "-", "?" ]
    # B = [ "1", "241", "1", "361", "241", "101" ]
    A = ["+", "+", "-", "?"]
    B = ["200", "200", "200", "0"]
    print(Solution.solve(Solution, A, B))