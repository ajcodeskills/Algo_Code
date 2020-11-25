#class for new Node
class Node:

	def __init__(self, data):
		
		self.data = data
		self.next = None
		self.prev = None

class DoubleLinked:

	def __init__(self):
		self.head = None
		self.tail = None

	def push(self, new_data):
		if self.head is None:
			self.head = Node(new_data)
			self.tail = self.head
		else:
			new_node = Node(new_data)
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = self.tail.next	
	
	def print_list(self):

		temp = self.tail
		while(temp):
			print(temp.data)
			temp = temp.prev

list2 = DoubleLinked()
list2.push(3)
list2.push(5)
list2.push(9)
list2.push(8)
list2.push(3)
list2.push(5)
list2.push(9)
list2.push(8)
list2.print_list()			
				