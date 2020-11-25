class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
class BST:
	def __init__(self):
		self.root = None
	def designBST(self, root, data):
		newnode = Node(data)
		if newnode.data <= root.data:
			if root.left is None:
				root.left = Node(data)
			else:
				return self.designBST(root.left, data)
		elif newnode.data > root.data:
			if root.right is None:
				root.right = Node(data)	
			else:
				return self.designBST(root.right, data)
	

		
				
	def printBST(self, root):
		while(root.left != None):
			print(root.data)
			self.printBST(root.left)
		while(root.right != None):
			print(root.data)	
			self.printBST(root.right)
		if(root.left == None and root.right == None):
			print(root.data)	
bst = BST()
arr = [2,5,3,7,4,8,5,9,56,0,5,3,2]
bst.root = Node(6)
for i in arr:
	bst.designBST(bst.root, i)
bst.printBST(bst.root)	

						


