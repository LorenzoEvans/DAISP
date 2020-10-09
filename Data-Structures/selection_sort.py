def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        
        # get the current value at the index of list
        value = arr[i]
        
        # to look left subract one from index
        left_index = i - 1
        print("i is: ", i)
        while value < arr[left_index] and left_index >= 0:
            
            
            # print(f'\nValues {value} is greater left_index {left_index}')
            # array in current position is swaped with array at previous position
            
            # Why can't we assign to array[i] if it is the same thing
            arr[left_index + 1] = arr[left_index]
            print("left_index is: ",left_index)
            left_index -= 1
            # print(arr)
        arr[left_index + 1] = value
    return arr

print(selection_sort([1, 9, 34, 12, 99, 2 , 4, 19]))