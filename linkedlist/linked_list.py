class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node
#getting the length of a linked list?
	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total

#display all elelemtns in the linked list on terminal in a list

	# Prints out the linked list in traditional Python list format. 
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

#get a certain element indexed in the linkedlist
#big o notation of O(n), more items in the list, more time to find that element
	# Returns the value of the node at 'index'. 

	def get(self,index):
		if index>=self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1
#removes a element from a specific index in the linkedlist
#usses garbage collection for deleting, all you need t know is th eprevious node, then ties it the the node after the current one your deleting
#so the th eindexed one is removed with garbage collection.			
#using big o notation, time complexity O(1), meaning its constant, knows exact location to delete element from
	# Deletes the node at index 'index'.
	def erase(self,index):
		if index>=self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Erase' Index out of range!")
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

	# Allows for bracket operator syntax (i.e. a[0] to return first item).
	def __getitem__(self,index):
		return self.get(index)


	#######################################################
	# Functions added after video tutorial

	# Inserts a new node at index 'index' containing data 'data'.
	# Indices begin at 0. If the provided index is greater than or 
	# equal to the length of the linked list the 'data' will be appended.
#using big o notation, time complexity O(1), meaning its constant, wont have to search entir list
#inserts/ a element into a specific index in the linkedlist, len increses of list! so changes the data in the sepcific index you want
	def insert(self,index,data):
		if index>=self.length() or index<0:
			return self.append(data)
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				new_node=node(data)
				prior_node.next=new_node
				new_node.next=cur_node
				return
			prior_node=cur_node
			cur_idx+=1

	# Inserts the node 'node' at index 'index'. Indices begin at 0.
	# If the 'index' is greater than or equal to the length of the linked
	# list the 'node' will be appended.

#inserts/replaces a node(diffrent from inserting data), into a specific index from the linked list
#so it keeps the data inside the node, but just changes the index location of the data
	def insert_node(self,index,node):
		if index<0:
			print("ERROR: 'Erase' Index cannot be negative!")
			return
		if index>=self.length(): # append the node
			cur_node=self.head
			while cur_node.next!=None:
				cur_node=cur_node.next
			cur_node.next=node
			return
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				prior_node.next=node
				return
			prior_node=cur_node
			cur_idx+=1

	# Sets the data at index 'index' equal to 'data'.
	# Indices begin at 0. If the 'index' is greater than or equal 
	# to the length of the linked list a warning will be printed 
	# to the user.
	def set(self,index,data):
		if index>=self.length() or index<0:
			print("ERROR: 'Set' Index out of range!")
			return
		cur_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				cur_node.data=data
				return
			cur_idx+=1

my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(8)
my_list.append(86)
my_list.append(34)


my_list.display()

#gives the length(total number of elements in the linked list)
print("Length: "+str(my_list.length()))


#getting a dpecific element from an index
print("element at 2nd index: %d" % my_list.get(2))

#removes the element from the given index
my_list.erase(1)
print("Length: "+str(my_list.length()))
my_list.display()
print('#########################')
#adds the element in a specific index
#adding new nodes, len of the elements increse after inserting a new element
my_list.insert(1, 2)
print("Length: "+str(my_list.length()))
my_list.display()
print('#########################')
print("element at 2nd index: %d" % my_list.get(2))
print("element at 3rd index: %d" % my_list.get(3))
#adds/replaces the node in a specific index
#my_list.insert_node(2, 3)
#print("Length: "+str(my_list.length()))
#my_list.display()



