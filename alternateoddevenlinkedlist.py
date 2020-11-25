class Node:
	def __init__(self, data):
		self.data = data
		self.next = next
#Alternate node deletion in singly linked list
def AltDelete(head):
	if head == None:
		return
	prev = head
	now = head.next
	while(prev != None and now != None):
		prev.next = now.next
		now = None
		prev = prev.next
		if(prev != None):
			now = prev.next

def newnode(key):
	temp = Node(0)
	temp.data = key
	temp.next = None
	return temp
def insertbeg(head, data):
	temp = newnode(data)
	temp.next = head
	head = temp
	return head
def altoddeven(head):
	odd = []
	even = []
	i = 1
	while(head != None):
		if(head.data % 2 != 0 and i%2 == 0):
			odd.append(head)
			
		elif(head.data % 2 == 0 and i%2 != 0):
			even.append(head)
		head = head.next
		i = i + 1		
	while(len(odd) != 0 and len(even) != 0):
		odd[-1].data, even[-1].data = even[-1].data, odd[-1].data
		odd.pop()
		even.pop()
	return head	
def splitlinkedlist(head):
	head1 = head
	head2 = head.next
	temp1 = head1
	temp2 = head2
	while(temp1.next != None):
		temp1.next = temp2.next
		temp1 = temp1.next
		temp2.next = temp1.next
		temp2 = temp2.next
	print("\n1st list:")	
	printlist(head1)
	print("\n2nd list:")
	printlist(head2)		

def printlist(node):
	while(node != None):
		print(node.data, end = " ")
		node = node.next


head = newnode(1)
head = insertbeg(head,0)
head = insertbeg(head,1)
head = insertbeg(head,0)		
head = insertbeg(head,1)
head = insertbeg(head,0)
head = insertbeg(head,1)
printlist(head)
#altoddeven(head)
#printlist(head)
#AltDelete(head)
#printlist(head)
splitlinkedlist(head)

