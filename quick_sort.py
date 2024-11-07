def partition(array, low, high):
    pivot = array[low]
    i = low +  1; 
    j = high; 
    #print(pivot, i)
    while(True): 
        while(i <= j  and pivot >= array[i]): 
            i += 1
        
        while(pivot <= array[j] and j >= i): 
            #print(pivot, array[j])
            j -= 1
        
        if(i >= j):
            break
        array[i], array[j] = array[j], array[i]
    
    
    array[j], array[0] = array[0], array[j]
    return j


def quicksort(array, low=0, high=None):
    if(high == None): 
        high = len(array) - 1
    #print(high, low)
    #print( array)
    if(low < high): 
        v = partition(array, low, high) 
      #  print(v, high, array); exit()
        quicksort(array, low, v-1)
        quicksort(array, v + 1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)

#Python