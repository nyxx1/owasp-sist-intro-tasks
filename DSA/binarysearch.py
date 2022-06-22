# ALGORITHM
# Sort the given list
# Find out the middle element's index using low(starting element) and high(last element) : low + high //2
# Return the middle index if it is equal to the key and terminate the search
# If the key element is greater than the mid element, eliminate left sublist and repeat step 2 and 3
# If the key element is less than the mid element, eliminate right sublist and repeat step 2 and 3

def binarysearch(list2,key):
	low = 0
	high = len(list2)-1
	mid = 0
	while low<=high:
		mid = (low+high)//2

		if key > list2[mid]:
			low = mid + 1
		elif key < list2[mid]:
			high = mid - 1
		else:
			return mid
			
list1=list(map(int,input().strip().split()))
list2=sorted(list1)
key = int(input())
key_index=binarysearch(list2,key)
print(key_index)

