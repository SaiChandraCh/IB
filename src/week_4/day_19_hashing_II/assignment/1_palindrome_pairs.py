class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def solve(self, A):
        map = {}
        for i in range(len(A)):
            map[A[i]] = i
        result = []
        for i in range(len(A)):
            prefix = ""
            sufix = ""
            for j in range(len(A[i])):
                prefix = A[i][j]+ prefix
                if prefix in map and i != map[prefix] and Solution.isPalindrome(Solution,A[i][j+1:]):
                    if [i,map[prefix]] not in result:
                        result.append([i,map[prefix]])
                sufix = sufix + A[i][len(A[i])-(j+1)]
                if sufix in map and i != map[sufix] and Solution.isPalindrome(Solution,A[i][:len(A[i])-(j+1)]):
                    if [map[sufix],i] not in result:
                        result.append([map[sufix],i])
        return result

    def isPalindrome(self,str):
        length = len(str)
        for i in range(length//2):
            if str[i] != str[length-(i+1)]:
                return False
        return True

if __name__ == '__main__':
    print(Solution.solve(Solution,
                         ["abc", "sa", "xy", "as"]
                         ))