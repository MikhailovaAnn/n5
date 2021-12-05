def medians(nums1, nums2=[]):
    massive = sorted(nums1 + nums2)
    if len(massive) % 2 == 1:
        return massive[len(massive) // 2]
    else:
        return (0.5 * (massive[len(massive) // 2 - 1] + massive[len(massive) // 2]))
