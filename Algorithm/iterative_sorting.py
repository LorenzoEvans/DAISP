# TO-DO: Complete the selection_sort() function below 

# def insertion_sort(arr):
#     for i in range(0, len(arr)):
#         cur_val = arr[i]
#         print(cur_val)
#         index = i
#         print("Outer index:", index)
#         while index > 0 and arr[index - 1] > cur_val:
#             arr[index] = arr[index - 1]
#             index -= 1
#             print("Inner index:", index)
#         arr[index] = cur_val
#     return arr

#  Conceptually, we split a collection into sorted and unsorted parts.
#  One part is the first element, and a single element list is always sorted.
#  For every index in the collection, we compare the value at index i,
#  with everything to the left of it, to figure out it's place in the sorted
#  sub-collection.

def insertion_sort(arr):
    for i in range(0, len(arr)):  # Every number between 0 and length of data set
        cur_val = arr[i]  # Capture array element selected on current iteration of for loop
        #print(cur_val)  # Printing for check
        index = i  # Set index to number indication which iteration is currently taking place
        #print("Index is:", index, "i is: ", i)
        while index > 0 and arr[index - 1] > cur_val:  # While index > 0 & the element of the arr at the index equaling index - 1 is greater than the current element
            #  arr[index - 1] doesn't trigger out of bounds because python lists loop around at -1, and 0 - 1 == -1
            arr[index] = arr[index - 1]  # set the current element to the value before it, because the current element is less than the previous one.
            index -= 1
        print(arr[index - 1])
        arr[index] = cur_val


rand_arr = [1, 4, 6, 3, 5, 2]

def insertion_sort(arr):
    for i in range(0, len(arr)):
        cur_val = arr[i] # arr[i => (0)] => 1 # arr[i => (1)] => 4 # arr[2] => 6 # 3
        index = i # index => 0 # index => 1 # index => 2 # 3
        while index > 0 and arr[index - 1] > cur_val:
	    # while 0 > 0 and arr[index (0) - 1 => -1 => (2)] 2 > 1
	    # while 1 > 0 and arr[index (1) - 1 => 0] => 1 > 4
	    # while 2 > 0 and arr[index (2) - 1 => 1] => 4 > 6
	    # while 3 > 0 and arr[index (3) - 1 => 2] => 6 > 3
	    # bc both false, 1 and two are *not* swapped.
	    # bc one false, nothing swapped, index not decremented
	    # bc both true, arr[3 => (3)] = arr[index => 3 - 1 => 2] => 6.
            arr[index] = arr[index - 1] # 3 & 6 are swapped
            index -= 1 # 3 - 2, we'll have 6 & 5, and swap again.
        print(arr[index - 1])
        arr[index] = cur_val
# An insertion sort requires a numerical range, from 0 to the length of the data set.
# This is easily done in the declaration of a loop.
# Next, it is customary to store an element of the data set in a variable, typically
# corresponding to the current stage of the iterative loop, which depends on the aforementioned numerical range.
# Also, it is customary to store the numerical representation of said stage within a variable as well.
# We then have a boolean condition, which checks if the current index is greater than 0, and if the stored element is less than the
# element located at the address represented by index - 1, and if both of these are true, then currently within our data set,
# we have a larger element, preceding a smaller element, which means we need to change these places, and decrement the index
# to start from the prior to last step, and continue searching.
# This algorithm is inefficient because while swapping these two values based on that criteria may be correct, relative to *each other*,
# it does not guarantee that this sorting is correct in the context of the *greater data set* the two values exist in, which leads to
# multiple passes to make sure every element is in the right order according to every other element, as opposed to just a given pair of elements.


# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = 0
#         # cur_val = arr[i]
#
#         smallest_index = cur_index
#
#         while smallest_index > cur_index:
#
#
#         # TO-DO: find next smallest element :: arr[i + 1]

#         # (hint, can do in 3 loc)
#
#
#
#
#         # TO-DO: swap :: cur_val
#
#
#
#
#     return arr
#

# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):
#
#     return arr
#
#
# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr

