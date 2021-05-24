# Python MaxHeap
# public functions: push, peek, pop
# private functions: __swap, __floatUp, __bubbleDown

#MaxhHap is fast!!!push:Insert in O(log n), peek:Get Max in O(1), and pop:Remove Max in O(log n)
#its super quick cause the maxvalue if always the number one value in the heap. so node 1 should be the maxheap 95, sort these nodes using an array
#What is a MaxHeap? Complete binary tree, bottom layer must be filled in from left to right, and every node must be <=(less than or equal) to its parent
#easy to implement using an array

#Push: add value to end of array, and Float it up to its proper postion
#Peak: return the value at heap[1]
#Pop: move max to end of array, by swaping the 1st item in the heap(max) for the last one,  save it as max value as you delete it, bubble down the item at index 1(last item in heap) to its proper postion, finally return the max value 


class MaxHeap:
	def __init__(self, items=[]):
		super().__init__()
		self.heap = [0]
		for i in items:
			self.heap.append(i)
			self.__floatUp(len(self.heap) - 1)

	def push(self, data):
		self.heap.append(data)
		self.__floatUp(len(self.heap) - 1)

	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False
			
	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1, len(self.heap) - 1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else: 
			max = False
		return max

	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		parent = index//2
		if index <= 1:
			return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(index, parent)
			self.__floatUp(parent)

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)

m = MaxHeap([95, 3, 21])
print(str(m.heap[0:len(m.heap)]))#prints list
print(str(m.pop())) #removes largest number from list
m.push(10)
m.push(110)
print(str(m.heap[0:len(m.heap)]))#prints list
print(str(m.peek())) #prints largest number in heap, 110
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop())) #removes largest number in heap, 110
print(str(m.heap[0:len(m.heap)]))
print(str(m.peek()))  #get 21 as the largest number in heap
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))#removes largest number in heap, 21
print(str(m.heap[0:len(m.heap)]))
