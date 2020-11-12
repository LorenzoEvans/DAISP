def removeDuplicates(self, nums: List[int]) -> int:
    # So, let's say we encounter a number,
    # and we want to check if it is a duplicate.
    # We can scan for numbers, and check the subsequent ones for matches.
    # If the next element is not a match, we can move to it, and compare to it.
    
    # If we encounter a match, we want to then scan for the first non-match,
    # and close the gap somehow.
        # We could del nums[i], until we get a non-match,
        # then move out pointer up.
        
    i = 0
    
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i + 1]
        else:
            i+=1
    return len(nums)
    