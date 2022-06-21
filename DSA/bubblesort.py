# Algorithm (ascending order)
# From index 0, compare the first element to to the adjacent element in the list
# if the current element is greater than the next element, swap.
# if the current element is less than the next element, move to the next element, repeat step 1

def bubblesort(list1):
	for j in range(len(list1)-1):
		for x in range(len(list1)-1):
			if list1[x] > list1[x+1]:
				list1[x],list1[x+1] = list1[x+1],list1[x]
	print(list1)

list1=list(map(int,input().strip().split()))
bubblesort(list1)

