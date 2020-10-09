# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  i = 0

  while i < len(arr):
    if arr[i] == target:
      return i
    i += 1
  return - 1
  # for i in arr:
  #   print(i)
  #   if arr[i] is target:
  #     return arr[i]
  #   else:
  #       return -1

randarr = [1, 2, 3, 4, 5 ]

print(linear_search(randarr, 3))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  mid = high / low

  # if arr[mid] == target:

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
