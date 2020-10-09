class Heap:
    """
        
    """
    def __init__(self):
        pass
    def heapify(self, arr, height, i):

        # [ | 0 | 1 | 2 | 3 | 4 ]
        # [ | 3 | 4 | 9 | 5 | 2 ]
        """
            So largest is i, which is at arr[0], which holds value 3.
            We next generate our child indexes:
                leftChildIndex = 2 * i + 1, which gives us 2 * 0 + 1, which evalutes to 1.
                    At arr[1], we have an element with value 4.
                rightChildIndex = 2 * i + 2, which gives us 2 * 0 + 2, which evaluates to 2.
                    At arr[2], we have an element with value 9.
            Now, we substitute these values into our conditional statements:
                if leftChildIndex is less than height (if 1 is less than 4), and arr[i] is less than arr[leftChildIndex] (if 3 is less than 4)
                    **Note** :: Height, is the length of the array that your heap is being built from.`
                    We want to set the largest variable to the value of leftChildIndex (be careful not to confuse this with the value `at`).
                if rightChildIndex is less than height (if 2 is less than 4), and arr[leftChildIndex] is less than arr[i] (if 4 is less than 3)
                    We want to set the largest variable to the value of the rightChildIndex
                if largest does not equal i (if 1 does not equal 0)
                    We want to swap arr[i] (3), and arr[largest] (4).
        """
        largest = i  # Select element at index i.
        l = 2 * i + 1 # The array index of the element for the left child of a node can be found
                      # at the index found at 2i + 1
        r = 2 * i + 2 # The array index of the right child, at 2i + 2. 
        if l < height and arr[i] < arr[l]:  # if the left child index is less than height, and the element at the current index,
                                            # is less than the element at the left child index,
                                            # we can set the largest index to the left child index,
            largest = l
        if r < height and arr[largest] < arr[r]:  # if the right child index, is less than height, and the element at the current index
                                                  # is less than the element, at the left child index,
                                                  # we can set the largest index to the right child index.
            largest = r
        if largest != i:
            print("arr[i] is: ", arr[i], "arr[largest] is", arr[largest])
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr, height, largest)

    def insert(self, array, newNum):
        size = len(array)
        if size == 0:
            array.append(newNum)
        else:
            array.append(newNum)
            for i in range((size//2)-1, -1, -1): # Still need to analyze this line, it boggles me.
                self.heapify(array, size, i)

    def deleteNode(self, array, num):

        size = len(array)
        i = 0

        for i in range(0, size):
            if num == array[i]:
                break
            
        array[i], array[size-1] = array[size-1], array[i]
        array.remove(size-1)
        
        for i in range((len(array)//2)-1, -1, -1):
            self.heapify(array, len(array), i)
    
arr = []
heap = Heap()
heap.insert(arr, 3)
heap.insert(arr, 4)
heap.insert(arr, 9)
heap.insert(arr, 5)
heap.insert(arr, 2)
# | 3 | 4 | 9 | 5 | 2

# def generic_heapify(arr, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#     length = len(array) - 1 # this probably represents the `height` of our tree.

#     if l <= length and array[i]

#     if l > arr[largest]

def build_heap(vals, i):
    for i in reversed(range(len(array)//2)):
        generic_heapify(vals, i)



heap.deleteNode(arr, 4)