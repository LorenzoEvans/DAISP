def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    
    start = count = 0
    # So we have two pointers here, and count is
    # our manual iterator.
    # current = start = 0
    # nums[start] = nums[0] = 1
    
    while count < len(nums):
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % len(nums)
            # 0 + 3 % 6 => 3
                # This tells us where our first number will go.
                # 1 will swap with the 3rd element.
            # 1 + 3 % 6 => 4
                # 2 will swap with the 4th element.
            # 2 + 3 % 6 => 5
            nums[next_idx], prev = prev, nums[next_idx]
                # nums[next_idx] is the item we're moving.
                # next_idx = the index to place our item in.
                # Prev is our *temp* variable.
            current = next_idx
            # Once we do our swap, we stay on the index
            # of the element we swapped *with*.
            count += 1
            # We increase count in order to meet the condition
            # that will allow us to exit our loop.
            if start == current:
                break
        start += 1
    print(nums)