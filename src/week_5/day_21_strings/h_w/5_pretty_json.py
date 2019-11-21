#
class Solution:
	# @param A : string
	# @return a list of strings
    def prettyJSON(self, A):
        result = ""
        for i in A.split(","):
            print(i)

if __name__ == '__main__':
    Solution.prettyJSON(Solution,'{"id":100,"firstName":"Jack","lastName":"Jones","age":12}')