# The COMP 2150 assignment was to modify Top's LinkedList implementation

'''
Basic implementation of a singly linked list

We want the list to support these operations:

- get: return the element at a specific index
- set: modify the element at a specific index
- add: insert a new element at a specific index
- delete: remove the element at a specific index (to be completed in HW 3)
'''

# This class represents a single node of the linked list
# Each node contains its data, and a reference to the next node in the list
class Node:
	# Constructor
	def __init__(self, data, next_node):
		self.data = data
		self.next_node = next_node


# This class represents a linked list - a collection of Node objects.  The list
# keeps track of the head node.  From there, we can get to any other node in
# the list by following the next_node references.
class LinkedList:
	# Constructor
	def __init__(self):
		# In an empty list, the head reference points to None
		self.head = None

		# This attribute keeps track of how many nodes are in the list
		# (handy for validating indices in some of the later methods)
		self.size = 0

	# The __str__ method traverses the list to see what data is inside
	# This is a O(n) algorithm - the amount of work done increases in a linear
	#  fashion with the size of the list (the plot of the work done vs. the
	#  list size is a straight line with positive slope)
	def __str__(self):
		result = 'head -> '

		# List traversal - we set up a new reference (temp) to the head, and
		# repeatedly move temp down the list until it points to None
		temp = self.head
		while temp != None:
			# Get temp's data
			result += str(temp.data) + ' -> '

			# Move temp to the next node in the list
			temp = temp.next_node

		result += 'None'
		return result


	# Returns the element at a specific index (must be non-negative), or raises
	# an error if an invalid index is provided
	def get(self, index):
		# Make sure index is valid
		if 0 <= index < self.size:
			# Move temp down the list index times
			temp = self.head
			for i in range(index):
				temp = temp.next_node

			# Return temp's data
			return temp.data
		else:
			raise IndexError(f'Invalid index provided: {index}, valid values are {0}-{self.size - 1}')


	# Changes the element at a specific index (must be non-negative), or raises
	# an error if an invalid index is provided
	def set(self, index, new_data):
		# Almost exactly the same code as get, except we *change* temp's data
		# rather than returning it after the traversal loop
		if 0 <= index < self.size:
			temp = self.head
			for i in range(index):
				temp = temp.next_node
			temp.data = new_data
		else:
			raise IndexError(f'Invalid index provided: {index}, valid values are {0}-{self.size - 1}')


	# Adds a new node to the head (front) of the list
	# This is a O(1) (constant time) algorithm - it always takes the same amount
	#  of work regardless of the size of the list
	def add_to_head(self, new_data):
		self.head = Node(new_data, self.head)
		self.size += 1

	# Adds a new node to any index of the list (index must be non-negative),
	# or raises an error if an invalid index is provided
	def add(self, index, new_data):
		# Index 0 is the head, so just call the existing add_to_head method
		if index == 0:
			self.add_to_head(new_data)

		# Check index to be sure it's valid
		# Note that self.size *is* a valid index here -- that means adding to
		#  the very end of the list
		elif 0 < index <= self.size:
			# Get to the node at (index - 1)
			temp = self.head
			for i in range(index - 1):
				temp = temp.next_node
			# Insert the new node after (index - 1)
			temp.next_node = Node(new_data, temp.next_node)
			self.size += 1
		else:
			raise IndexError(f'Invalid index provided: {index}, valid values are {0}-{self.size}')


	# Removes the first (head) node from the list, or raises an error if the
	# list is empty
	def delete_from_head(self):
		if self.size > 0:
			self.head = self.head.next_node
			self.size -= 1
		else:
			raise ID10TError()


	# The linear search algorithm, adapted for a linked list
	def linear_search(self, target):
		# Repeatedly calling get is not efficient -- *each* call to get
		# requires traversing the list from the head
		# for i in range(self.size):
		# 	if self.get(i) == target:
		# 		return i
		# return False

		# Better: just traverse the list once
		temp = self.head
		index = 0
		while temp != None:			# List traversal loop
			if temp.data == target:
				return index
			temp = temp.next_node
			index += 1

		return False


	# Returns the average of all numeric elements in the list, or None if there
	# are no such elements
	def average(self):
		sum_numbers = 0
		qty_numbers = 0

		temp = self.head
		for i in range(self.size):	# Another way to write a list traversal loop
			# Not every node is guaranteed to have numeric data - check if
			# this node's data is an instance of int or float
			if isinstance(temp.data, (int, float)):	# Same as isinstance(temp.data, int) or isinstance(temp.data, float):
				sum_numbers += temp.data
				qty_numbers += 1
			temp = temp.next_node

		if qty_numbers > 0:
			return sum_numbers / qty_numbers

		# return None is implied if qty_numbers is 0
	def delete(self, index):
		# deletes the element at arg index from list. raise IndexError if invalid
		if 1 <= index < self.size:
			next = self.head
			prev = self.head
			i = 0
			while i < index:
				if i == (index - 1):
					prev = next
				next = next.next_node
				i += 1
			if next:
				prev.next_node = next.next_node
			else:
				prev.next_node = None
			self.size -= 1
			return
		raise IndexError(f'Invalid index provided: {index}, valid values are {0}-{self.size - 1}')
	
	def delete_target(self, target):
		# deletes the target while only traversing 
		prev = None
		next = self.head
		while next != None:
			if next.data == target:
				if prev == None:
					self.head = next.next_node
					self.size -= 1
					return next
				elif prev:
					prev.next_node = next.next_node
					self.size -= 1
					return next
			else:
				prev = next
				next = next.next_node
		return None
	
	def __eq__(self, other):
		if isinstance(other, LinkedList):
			if self.size == other.size:
				next1, next2 = self.head, other.head
				while next1:
					if next1.data != next2.data:
						break
					next1 = next1.next_node
					next2 = next2.next_node
				else: # won't execute if break
					return True
		return False

# Example of a custom exception type -- simply create a subclass of Exception
class ID10TError(Exception):
	# No need to do anything else
	pass

# Test code

# print('\nTests for linear_search...')
stuff = LinkedList()
for d in range(20, 0, -1):
	stuff.add_to_head(d)
# print(stuff)

# for t in range(1, 21):
# 	print(stuff.linear_search(t))
# print(stuff.linear_search(100))
# print(stuff.linear_search(-100))

# print('\nTests for average...')
stuff2 = LinkedList()
data = [10, 0.5, 4, 'sloth', 5.5, '4']
for e in data:
	stuff2.add(0, e)
# print(stuff2)
# print(stuff2.average())

# 1d
def copy(list1):
	result = LinkedList()
	next = list1.head
	i = 0
	while next != None:
		result.add(i, list1.get(i))
		next = next.next_node
		i += 1
		
	return result

def diff(l1, l2):
	return f'\n {l1}\n ↓\n {l2}'

stuff_copy = copy(stuff)

# delete from head of list with several nodes
stuff_copy.delete(1)
print('stuff == stuff_copy after delet 1?', stuff == stuff_copy)
# print(stuff_copy)
print ('test for obvious inequality: ', stuff == stuff2) # test for obvious inequality

# delete from middle of list with several nodes
stuff2_copy = copy(stuff2)
print(stuff2_copy.size)
stuff2_copy.delete(3)
print(f'delete from middle of list (index {3}) of several nodes: {diff(stuff2, stuff2_copy)}')

# delete from tail of list with several nodes:
stuff2_copy.delete(stuff2_copy.size - 1)
print(f's2c now:\n {stuff2_copy.size} : {stuff2_copy}')

# delete_target from the head of a list with several nodes
stuff2.delete_target('4')
print(f'stuff2 after delet head: {stuff2}')

# delete_target from the middle of a list with several nodes
stuff2.delete_target('sloth')
print(f'stuff2 after delet sloth:\n {stuff2}')

# delete_target from the tail of a list with several nodes
stuff2.delete_target(10)
print(f'stuff2 after delet tail 10:\n {stuff2}')

# delete_target from a non-empty list that does not even have that target
print(stuff2.delete_target('4'))

# delete_target from an empty list
emptylist = LinkedList()
print(emptylist.delete_target('4'))

# equal for two equal lists
stuff3 = copy(stuff)
print(stuff == stuff3)

# equal for two lists with same elements to some point but one list ends and the other keeps going
data2 = [1, 2, 3, 4, 56, 28, 12, 'u']
data2_copylongertho = [1, 2, 3, 4, 56, 28, 12, 'u', 'v', 1211]
eq3lu = LinkedList()
eq3lu2 = LinkedList()
for i in range(len(data2), 0, -1):
	eq3lu.add_to_head(i)
for v in range(len(data2_copylongertho), 0, -1):
	eq3lu2.add_to_head(v)
print(f'equal for two lists with same elements until a certain point then one list ends and the other keeps going: {eq3lu == eq3lu2}')

# eq between two lists of same number elements, but not all elements match one another
eq3lu2 = LinkedList()
for j in range(len(data2), 0, -1):
	eq3lu2.add_to_head(j)
data2_flipped = [1, 3, 2, 4, 56, 28, 12, 'u']
print(f'eq between 2 lists same len but not all ∈ match: {eq3lu2 == eq3lu}')

# eq between  non-empty list and an empty list
print(f'nonempty list vs empty list: {eq3lu == emptylist}')

# eq between 2 empty lists
emptylist2 = LinkedList()
print(f'eq 2 empty lists: {emptylist == emptylist2}')

# non-empty list and a non-LinkedList
print(f'eq non-empty and non LinkedList: {eq3lu == ["meow"]}')


