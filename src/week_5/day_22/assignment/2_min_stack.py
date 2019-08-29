class MinStack:
    stack = []
    min = None
    # @param x, an integer
    def push(self, x):
        # print("push : ",x)
        if len(self.stack) == 0:
            self.stack.append(x)
            self.min = x
        else:
            if x<self.min:
                self.stack.append(2*x-self.min)
                self.min = x
            else:
                self.stack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack)>0:
            temp = self.stack.pop()
            # print("pop : ",temp)
            if temp < self.min:
                self.min = 2* self.min - temp
                # print(self.min)

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        if self.min:
            temp = self.stack[len(self.stack)-1]
            if temp < self.min:
                return self.min
            return temp
        return -1

    # @return an integer
    def getMin(self):
        return self.min if len(self.stack)>0 and self.min else -1

if __name__ == '__main__':
    print(MinStack.getMin(MinStack))
    print(MinStack.top(MinStack))
    print(MinStack.top(MinStack))
    print(MinStack.getMin(MinStack))
    MinStack.push(MinStack,593848644)
    print(MinStack.top(MinStack))
    MinStack.pop(MinStack)
    print(MinStack.top(MinStack))
    print(MinStack.top(MinStack))
    print(MinStack.top(MinStack))
    print(MinStack.top(MinStack))