class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return a strings
    def solve(self, A, B, C):
        days = (C-1)*365 + (C-1)//4 + (A-1)
        for i in range(1,B):
            if i%2 != 0:
                days += 31
            else:
                days += 30

        if B>1:
            if C%4 == 0:
                days -= 1
            else:
                days -= 2

        if days%7 == 1:
            return "monday"
        elif days%7 == 2:
            return "tuesday"
        elif days%7 == 3:
            return "wednesday"
        elif days%7 == 4:
            return "thursday"
        elif days%7 == 5:
            return "friday"
        elif days%7 == 6:
            return "saturday"
        else:
            return "sunday"

if __name__ == '__main__':
    print(Solution.solve(Solution,
                         19,4,2019))# friday
                         # 1, 1, 2))