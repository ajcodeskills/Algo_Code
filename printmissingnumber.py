import array
def printmissing(arr, size):
	limit = 100
	l = array.array('i',[0] * 200)
	for i in range(0,limit):
		l[i] = False
	for i in arr:
		if i < limit:
			l[i] = True
	i = 0		
	while(i<limit):
		if l[i] == False:
			j = i+1
			while(j<limit and l[j] == False):
				j += 1
			p = j-1
			if(i+1)==j:
				print(i)
			else:
				print("%d - %d" %(i,p))	
			i = j
		else:
			i += 1
lst = [121,21,455,5,600,98,67,33,92,1230,66,77,800,90,100]
size = len(lst)
printmissing(lst, size)	

#100% CORRECT
