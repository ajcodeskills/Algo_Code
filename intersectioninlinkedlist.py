from SinglyLinked import Node, Singlylinkedlist
def intersectionoftwolist(head1, head2):
	temp1 = head1
	temp2 = head2
	dnode = Node(0)
	head = dnode
	while(temp1 != None):
		if(temp1.data != temp2.data):
			temp1 = temp1.next
		if(temp1.data == temp2.data):
			dnode.next = temp1
			dnode = dnode.next
			temp1 = temp1.next
			temp2 = temp2.next
	return head.next

def segregateevnodd(head):
	i = 0
	while(i<2):

		if(head.data%2==0):
			even = head
			even1 = even
			
		else:
			odd = head
			odd1 = odd
		head = head.next	
		i = i + 1		
	
		
	temp = head	
	while(temp != None):
		if(temp.data%2 == 0):
			even.next = temp
			even = even.next
		else:
			odd.next = temp
			odd = odd.next
		temp = temp.next	
	even.next = odd1
	odd.next = None
	return even1	

def printlist(head):
	while(head != None):
		print(head.data)
		head = head.next	
list1 = Singlylinkedlist()
list2 = Singlylinkedlist()
list1.push(8)
list1.push(7)
list1.push(6)
list1.push(5)
list1.push(4)
list1.push(3)
list1.push(2)
list1.push(1)
list2.push(12)
list2.push(10)
list2.push(8)
list2.push(6)
list2.push(4)
list2.push(2)
print("List 1 data:")
list1.printlist()
print("List 2 data:")
list2.printlist()
head = intersectionoftwolist(list1.head, list2.head)
print("Intersection List:")
printlist(head)
print("Segregate of even and odd:")
seg = segregateevnodd(list1.head)
printlist(seg)
