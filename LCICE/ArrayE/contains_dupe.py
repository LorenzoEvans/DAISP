def containsDuplicate(self, nums: List[int]) -> bool:
    
    # So what we want to do, is create a hash-table in order to keep track,
    # of occurences.
    
    # Then we can take all the occurrence values that exist
    # in the hashtable, and check them.
    
    # If any one of them is greater than one,
    # we can confirm duplicates.
    
    # If none of them are, there are none
    if len(nums) == 0:
        return False
        
    dupes = {}
    
    for i in range(len(nums)):
        if nums[i] not in dupes:
            dupes[nums[i]] = 1
        else:
            return True
    count_arr = list(dupes.values())
    
    count_arr.sort()
    
    if count_arr[-1] == 1:
        return False
    else:
        return True
    
    print(count_arr)
    # return True if len(set(nums)) < len(nums) else False
    