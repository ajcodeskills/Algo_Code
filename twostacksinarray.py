import array
import sys
class Twostacks:
	def __init__(self, arr, n):
		self.arr = arr
		self.n = n
		self.top1 = -1
		self.top2 = self.n
	def push1(self, x):
		if(self.top1 <= self.top2-1):
			self.top1 += 1
			self.arr[self.top1] = x
		else:
			print("Overflow")
	def push2(self, x):
		if(self.top2 > self.top1+1):
			self.top2 -= 1
			self.arr[self.top2] = x
		else:
			print("Overflow")
	def printarray(self, arr):
		for i in arr:
			print(i)
			
arr = array.array('i',[0]*50)
n = len(arr)
s = Twostacks(arr, n)
for i in range(20):
	s.push1(i)
	s.push2(i*3)
s.printarray(arr)	

