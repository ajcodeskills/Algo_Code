import array
def leadersofarray(arr):
	size = len(arr)
	max_from_right = arr[size-1]
	for i in range(size-1, -1, -1):
		if max_from_right < arr[i]:
			max_from_right = arr[i]
			print(max_from_right)

arr = array.array('i', [1,1,1,4,1,2,1,1,1,2,1,4,1])
size = len(arr)
leadersofarray(arr)

#Time Complexity = O(n)