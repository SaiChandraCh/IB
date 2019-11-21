class Node:
    val = 0
    next = None
    def __init__(self,val):
        Node.val = val
        Node.next = None

class LinkedList:
    head = None
    def __init__(self):
        self.head = None

    def insert_node(self,position, value):
        # @param position, an integer
        # @param value, an integer
        if not self.head:
            self.head = Node(value)
        else:
            temp = Node(value)
            curr = self.head
            prev = self.head
            while position > 0:
                prev = curr
                curr = curr.next
                position -= 1
            prev.next = temp
            temp.next = curr

    def delete_node(self,position):
        # @param position, integer
        # @return an integer
        temp = self.head
        prev = self.head
        while position > 0 and temp:
            prev = temp
            temp = temp.next
            position -= 1
        prev.next = temp.next

    def print_ll(self):
        # Output each element followed by a space
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    LinkedList.insert_node(LinkedList,position,value)

def delete_node(position):
    # @param position, integer
    # @return an integer
    LinkedList.delete_node(LinkedList,position)

def print_ll():
    # Output each element followed by a space
    LinkedList.print_ll(LinkedList)

insert_node(0,1)
insert_node(1,2)
insert_node(2,3)
insert_node(1,4)
print_ll()
# delete_node(0)
# print_ll()