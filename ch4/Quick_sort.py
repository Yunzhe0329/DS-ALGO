#choose pivot then divide into lower array & greater array ,then recursion
#Base case : array is null or have only one elements
def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot  = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return qsort(less)+[pivot]+qsort(greater)
print(qsort([2, 5, 1, 10]))