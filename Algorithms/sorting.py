# Bubble Sort

nums = [99,44,6,2,1,5,63,87,283,4,0]
# length = 11
# index length = 10

def bubbleSort(array):
    qw=0
    while qw < len(array)-1:
        for i in range(0,len(array)-1,1): # 0 to 10 loops
            if array[i] > array[i+1]: # If first element is less than second element
                temp = array[i] # Save first element to be reassigned
                array[i] = array[i+1] # First element becomes second element: [44,99]
                array[i+1] = temp # Second element becomes first element
        qw+=1
    return array


print(bubbleSort(nums))

# Selection Sort
def selectSort(array):
    for i in range(len(array)-1): # 0 to last index (length-1)
        min_index = i # Assume first element is lowest
        
        for j in range(i+1, len(array)-1): # j loops over remaining elements
            # If element at j is lower than min_index, update it
            if array[j] < array[min_index]: 
                min_index = j
        
        array[i] = array[min_index]
        array[min_index] = array[i]
    return array
print(selectSort(nums))

# Insertion sort

def insertSort(array):  
    for i in range(1,len(array)-1): # All values after first one (unsorted sublist)
        value_to_sort = array[i] 

        # IMPORTANT: 
        # while the left most value (i-1) is greater than value that is added to sorted sublist do this:
        # Also python does negative indexing, so i>0
        while array[i-1] > value_to_sort and i > 0:
            # Swap values:
            array[i] = array[i-1] 
            array[i-1]= array[i]
            i = i-1 # Use this to look at the left again
    return array

print(insertSort(nums))

# Merge Sort and O(nlog(n)) 