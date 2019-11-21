class Solution:
	# @param A : list of strings
	# @return an integer
    def evalRPN(self, A):
        stack = []
        for i in A:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(i)
            elif i == '+' :
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif i == '-' :
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif i == '*' :
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
            elif i == '/' :
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a//b)

        return stack.pop()
if __name__ == '__main__':
    print(Solution.evalRPN(Solution,
                           ["4", "13", "5", "/", "+"]))
                           # ["2", "1", "+", "3", "*"]))