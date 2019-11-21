class MinStack:
    stack = []
    min = None
    length = 0

    def __init__(self):
        MinStack.stack = []
        MinStack.min = None
        MinStack.length = 0

    # @param x, an integer
    def push(self, x):
        if MinStack.length == 0:
            self.stack.append(x)
            self.min = x
        else:
            if x < self.min:
                self.stack.append(2 * x - self.min)
                self.min = x
            else:
                self.stack.append(x)
        MinStack.length += 1

    # @return nothing
    def pop(self):
        if MinStack.length > 0:
            temp = self.stack.pop()
            if temp < self.min:
                self.min = 2 * self.min - temp
            MinStack.length -= 1

    # @return an integer
    def top(self):
        if MinStack.length == 0:
            return -1
        if self.min:
            temp = self.stack[-1]
            if temp < self.min:
                return self.min
            return temp
        return -1

    # @return an integer
    def getMin(self):
        return self.min if MinStack.length > 0 else -1

if __name__ == '__main__':
    ip = "g g p P 902892252 t p t t t P 27298395 p p p t p P 568806754 P 956103356 t P 777673740 t g P 954346459 t p t g P 295782020 t P 120122664 t p t g p g P 331028507 g P 476343064 t p P 145748285 g P 818485992 P 337179633 p P 495141134 p g t t t g P 595082937 t t p p g t P 876155364 p t P 609966381 P 285122553 P 245927531 p t t P 632360073 P 671026662 p P 304873227 g P 967040267 g P 540044673 g t P 943723110 g P 276569042 P 422454462 P 122470963 p t P 558756269 P 579233720 g t g t t t P 422414516 p g P 51794497 t t P 729600478 t g P 879525435 P 720601305 t t t p P 879953035 g t g p p P 757387396 p t p p P 625779954 g p p t p p p g g g P 900937019 P 579598217 p P 492468948 P 627662644 P 915236671 t t P 758312021 P 231671551 t t g p t t g g P 956987115 p g t P 953697104 t g p t P 479718872 t g P 994944195 t p t P 206013521 p P 229289988 t p g g p p g t P 919759358 t p t t p t t p p g t t g P 366592668 p P 39678727 g t P 801235875 g p t p p g t g g g t t t p P 921070466 p p t t p t t p P 369228095 t p P 34214952 t g t P 862725586 P 74006373 P 623678843 P 423943326 t p p t P 82194288 g t p p g t t t P 172903393 P 884778994 P 20319486 p t p t P 260199906 t t g p p g P 107786323 t p P 401456613 P 953065679 t t P 705472125 P 973879551 p p p t p P 998055709 P 178293825 P 123672964 t P 10883388 p P 924818709 g P 677126537 P 243069508 t p p p t p g P 328293663 t p t p p p p t t p p t p t P 635971737 t P 940282504 t P 835956584 t P 135413411 p g p P 527649189 t P 407302318 P 340313384 g p P 2693306 p p P 162477549 t t p g P 987759031 p p t g p P 589725944 p t P 13759741 g g t P 52431672 t t t p p P 904224899 P 733589294 g g P 10885030 p t t P 663049572 g t g p t p P 790483844 P 172169408 p g g p p g g p p t g p p t p t P 802717466 P 107813721 g g t g g p g t g g P 54875080 t t t t g g p p P 691145787 t g t P 264974253 g P 13929603 t P 349747565 P 233127098 t P 140360629 t g g t p p P 863679398 p g g p t t p p P 462545123 g p p g t t t t t g p P 727239358 p t g g g t P 855786744 P 226574555 P 55975954 P 997927283 g t p p g p t P 349040057 p t g t t p g t p t P 389310081 p g t t t t g g p P 828035712 t t p P 371574368 P 68190342 t P 143605337 p p P 467613260 t t t g t p t P 452028416 P 347173502 g P 795914831 P 209566311 g P 299386629 t g g t p P 131111913 p P 571170876 t p p p p t t g g P 176183041 P 427310004 t P 954801647"
    ip = ip.split(" ")
    i = 0
    result = []
    while i < len(ip):
        if ip[i] == "g":
            result.append(MinStack.getMin(MinStack))
        elif ip[i] == "p":
            result.append(MinStack.pop(MinStack))
        elif ip[i] == "t":
            result.append(MinStack.top(MinStack))
        elif ip[i] == "P":
            result.append(MinStack.push(MinStack,int(ip[i+1])))
            i += 1
        i+=1
    print(result)