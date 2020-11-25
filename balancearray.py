def rotatearray(arr, d, n):
    n = len(arr)
    reversearray(arr, 0, d-1)
    reversearray(arr, d, n-1)
    reversearray(arr, 0, n-1)
    return arr

def reversearray(arr, start, end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
T = int(input())

n, d = input().split()
d = int(d)
n = int(n)
arr=list(map(int,input().split()))
print(rotatearray(arr, d, n))