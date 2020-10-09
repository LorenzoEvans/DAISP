from typing import List
# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     # Alright so we want to iterate through a list in better than O(n) time.
    
#     # The next step up is logarithmic time, which we know generally means
#     # that the size of the data set we're working with will decrease as
#     # we iterate through it.
    
#     # Knowing that, we can whittle down our solution space by thinking 
#     # only about solutions that allow us to "disregard" some of the data in every iteration.
    
#     # Perhaps, instead of looping through the array, we can capture an element
#     # the array, and then do a constant check to see if that element exists elsewhere
#     # in the array, which will represent the frequency of the element.
    
#     # Another way to decrease the size of the data set, is to delete any element we 
#     # can confirm only exists in the array once- it's frequency is 1.
    
#     # If we do this at the beginning, we can decrease the size of the data set
#     # before we even get to doing the 'intensive' work.
    
#     # Since we're going to be able to delete every element from the array, we can 
#     # use a while loop, with a base case of len(nums) >= 0.
    
#     # We're going to want to return an array, so we will need a result array variable.
#     # result = []
    
#     # We will also bring in a dictionary, in order to match elements to frequencies.
#     # freq_dict = {}
    
#     # We're going to iterate manually, so we'll need an iterator variable.
#     # itrn = 0
    
    
#     # cur_element = array[iter] # Capture the first element of the array:
    
#     # freq_dict[cur_element] = 1 # Handle the initialized frequency here
#     # Remove the element.
#         # We're either removing a counted instance of a singular element,
#         # or a counted instance of a duplicate- either way removing it shouldn't harm
#         # our result, but should boost our efficiency slightly!
#     # del array[iter]
    
#     # While our array is not empty:
#         # Option 1: For i in range len(0, array[iter:len(array)]):
#                         # if array[i] == cur_element:
#                             # freq_dict[cur_element] += 1
#                         # if array[i] != cur_element and i == len(array):
#                             # del array[array.index(cur_element)]
#                             # (possibly recurse here)
#         # Option 2: while iter =< len(array):
#                         # if array[iter] == cur_element && in freq_dict:
#                             # freq_dict[cur_element] += 1
#                         # # if array[iter] == cur_element && not in freq_dict:
#                             # add element to dictionary
#                             # freq_dict[cur_element] = 1
#                             # del array[iter]
#                         # elif array[iter] != cur_element:
#                         # iter += 1
#         #         # elif iter > len(array):
#                     # At this point, we've either iterated through, and found a match
#                     # or we've iterated through and not found a match.
#                     # If there's a match, we incremented the value,
                
#     result = [] # Hold return values.
#     freq_dict = {} # Assoc values with frequencies.
#     itrn = 0 # Manual iterator.
#     freq_dict[nums[0]] = 1 # Record first frequency
#     del nums[0] # Delete recorded instance
#     # We're torn between two processes, one where we continuously lopp the first element off
#     # The other where we iterate through a continuously shrinking list
#         # This is the process that allows us to sneak below n!
#     fst_iter = 0
#     snd_iter = fst_iter + 1
#     while len(nums) >= 0 and itrn >= len(nums):
#       cur_element = nums[fst_iter]
#       nxt_element = nums[snd_iter]
#     print(freq_dict)

nums = [3,0,1,0]



def freq_nums(nums: List[int], k: int):
  freq_dict = {}
  a, *tail = nums
  freq_dict[a] = 1
  result = []
  while tail is not None and len(nums) > 1:
    nums = tail
    a, *tail = nums
    print(a, freq_dict)
    if a in freq_dict:
      freq_dict[a] += 1
      del nums[a]
    elif a not in freq_dict:
      freq_dict[a] = 1
    else:
      freq_nums(nums, k)
  
  freq_list = list(freq_dict)
  for i in range(0, k):
    # print(freq_list[i])
    result.insert(i, freq_list[i])
  return result[0]
  


print(freq_nums(nums, 1))