def singleNumber(self, nums: List[int]) -> int:
    # Could you implement a solution w/ a linear runtime complexity and without using extra memory?
    
    dupes = {}
    
    for i in range(len(nums)):
        if nums[i] not in dupes:
            dupes[nums[i]] = 1
        else:
            dupes[nums[i]] += 1
    for (ele, freq) in dupes.items():
        if freq == 1:
            return ele
    print(dupes)