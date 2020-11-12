def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    result = {}
    for i in range(len(nums1)):
        if nums1[i] not in result:
            result[nums1[i]] = 1
        else:
            result[nums1[i]] += 1
    k = 0
    
    for i in range(len(nums2)):
        if nums2[i] in result and result[nums2[i]] > 0:
            nums1[k] = nums2[i]
            k += 1
            result[nums2[i]] -= 1
    return nums1[:k]