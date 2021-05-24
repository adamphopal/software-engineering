# YouTube Link: https://www.youtube.com/watch?v=FSsriWQ0qYE
#Data Structures in Python: Singly Linked Lists -- Insertion
#how one may insert data into a linked list.
#We investigate three different insertion methods:

# 1. Append (add element to end of list)
# 2. Prepend (add element to beginning of list)
# 3. Add element after element in the list. 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node


llist = LinkedList()
llist.append("A")  #Append (add element to end of list)
llist.append("B")
llist.append("D")

llist.print_list()
print("###################")
llist.prepend("E") #Prepend (add element to beginning of list)
llist.print_list()
print("###################")
llist.insert_after_node(llist.head.next.next, "C") # Add element after element in the list. 
llist.print_list()
#final output: EABCD
