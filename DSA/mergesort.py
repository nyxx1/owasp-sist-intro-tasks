# ALGORITHM:
# Find the middle index of the list 
# Split the list into left and right sublists from the middle index
# Split the list until there is only one element in the sublists
# Compare and merge the sublists into single sorted list

def mergesort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left = list1[:mid]
        right = list1[mid:]

        mergesort(left)
        mergesort(right)

        i=0
        j=0
        k=0

        while len(left)>i and len(right)>j:
            if left[i]<right[j]:
                list1[k] = left[i]
                i+=1
            else:
                list1[k] = right[j]
                j+=1
            k+=1

        while len(left)>i:
            list1[k] = left[i]
            i+=1
            k+=1

        while len(right)>j:
            list1[k] = right[j]
            j+=1
            k+=1

list1=list(map(int,input().strip().split()))
mergesort(list1)
print(list1)


