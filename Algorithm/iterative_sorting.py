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

def insert_sort(arr):

    ''' 
    Given, rand_arr = [1, 4, 6, 3, 5, 2], let's observe this algorithm.
    We first select the 0th element of the array, which is arr[i], equaling 1.
    We then declare an index variable, initialized the value of i.

    While the index is greater than 0, and the element at arr[index - 1] is greater
    than arr[i] (1), we want to do some swapping.
        Because arr[index - 1] (2) is > 1,

    '''
    for i in range(0, len(arr)):
        cur_val = arr[i]
        index = i
        while index > 0 and arr[index - 1] > cur_val:
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = cur_val
def insertion_sort(arr):
    for i in range(0, len(arr)):
        cur_val = arr[i] # arr[i => (0)] => 1 # arr[i => (1)] => 4 # arr[2] => 6 # 3
        index = i # index => 0 # index => 1 # index => 2 # 3
        while index > 0 and arr[index - 1] > cur_val:
	    # while 0 > 0 and arr[index (0) - 1] => arr[-1] => arr[(2)] => 2 > 1
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


def selection_sort( arr ):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


# # TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    end_list = len(arr)
    for i in range(end_list):
        cur_val = arr[i]
        if cur_val > arr[i + 1]:
            cur_val, arr[i + 1] = arr[i + 1], cur_val
            end_list -= 1
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.genre = genre
        self.author = author
    def __repr__(self):
        return 'Title: ' + self.title, 'Author: ' + self.author, 'Genre: ' + self.genre

def insort(shelf):
    for index in range(len(shelf)):
        cur_book = shelf[index]  # your i
        book_idx = index

        while book_idx > 0 and cur_book.title.upper() < shelf[book_idx - 1].title.upper():
            shelf[index], shelf[index - 1] = shelf[index - 1], shelf[index]
            book_idx -= 1
    return shelf

book_shelf = [
Book('Lost In Math', 'Physics', 'Hossenfelder'),
Book('Against Method', 'Philosophy', 'Feyerabend'),
Book('Combinatorial Topology', 'Mathematics', 'Henle'),
Book('Single Variable Calculus', 'Mathematics', 'Steward'),
Book('Prolegomena', 'Philosophy', 'Kant')]

# book_shelf.append(Book('Against Method', 'Philosophy', 'Feyerabend'))
# book_shelf.append(Book('Combinatorial Topology', 'Mathematics', 'Henle'))
# book_shelf.append(Book('Critique of Pure Reason', 'Philosophy', 'Kant'))
# book_shelf.append(Book('Lost In Math', 'Physics', 'Hossenfelder'))
# book_shelf.append(Book('Single Variable Calculus', 'Mathematics', 'Steward'))
# book_shelf.append(Book('Working In Public', 'Technology', 'Eghbal'))

# print(insort(book_shelf))
insort(book_shelf)
for i in book_shelf:
    print(i.__repr__())


def quicksort(array):
    if len(array) < 2:
        # Base case: arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # Recursive case
        pivot = array[0]
        # Sub-array of all the elements less than the pivot
        less = [ i for i in array[1:] if i <= pivot]
        # Sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)