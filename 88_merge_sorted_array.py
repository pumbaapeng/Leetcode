class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ins = m + n - 1
        i1 = m - 1
        i2 = n - 1
        while i1 >= 0 or i2 >= 0:
            if i1 < 0 or (i1 >= 0 and i2 >= 0 and nums2[i2] > nums1[i1]):
                nums1[ins] = nums2[i2]
                i2 -= 1
            else:
                nums1[ins] = nums1[i1]
                i1 -= 1
            ins -= 1
