class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Alright so, we can't brute force this, but 
        # let's walk through it a bit anyway.
        # Maybe we do a greedy algorithm?
            # So we select nums[0], which is -2.
                # Compare to next?
                # If the number after this is greater than it,
                # than maybe we start there,
        sub_arr = []
        max_val = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                prev_max = max_val
                max_val = nums[i]
        # So we can grab the max_value we need (4),
        # now we need to confirm that it's the 1st four we find.
        sum_val = 0
        sum_val += max_val
        max_val_idx = nums.index(max_val)
        nums = nums[max_val_idx:]
        
        # print("max_val: ", max_val, "prev_max: ", prev_max)
        # print(nums)
        # Alright, now we're to the meat of the problem:
            # We need to push everything after 4, up until -5 (excl),
            # into an array.
            # 4 + -1 => 3
            # 3 + 2 => 5
            # 5 + 1 => 6
            # 6 + -5 => 1 > 4
        while max_val <= sum_val and len(nums) > 0:
            cur_val = nums.pop(0)
            print("cur_val: ", cur_val)
            sum_val += cur_val
            print("sum_val: ", sum_val)
            sub_arr.append(cur_val)
            print("max_val: ", max_val)
            # So, now that we have a start, we can continue adding
            # subsequent elements, while keeping track of the prev_max
            
            # If our addition, ends up bringing us back to the prev_max,
            # then, our addition must not have started at the right place,
            # as the largest sub_array sum, should always be greater than, 
            # (or equal to), the previous max, because if it's less than the previous 
            # that means we could have a larger sub_array, by incoroporating that number.
        print(sub_arr)