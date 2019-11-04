class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return [s[0]]
        return Solution.reverseString(Solution, s[1:]) + [s[0]]

if __name__ == '__main__':
    print(Solution.reverseString(Solution,["h","e","l","l","o"]))
    # print(Solution.str)


# class Solution:
#     def reverseString(self, s: [str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         Solution.util(Solution, s, 0, len(s) - 1)
#
#     def util(Solution, s, l, r):
#         if r > l:
#             if l == r:
#                 return s
#             s[l], s[r] = s[r], s[l]
#             return Solution.util(Solution, s, l + 1, r - 1)