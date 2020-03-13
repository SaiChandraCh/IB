class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        map = {}
        length = len(A)
        for i in range(length):
            temp = list(A[i])
            temp.sort()
            temp = ''.join(temp)
            if temp not in map:
                map[temp] = [i+1]
            else:
                map[temp].append(i+1)
        result = []
        for key in map:
            result.append(map[key])
        return result

if __name__ == '__main__':
    print(Solution.anagrams(Solution,['cat','dog', 'god', 'tca']))