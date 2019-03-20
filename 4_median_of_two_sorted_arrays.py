# Lesson
# 1) find k-th in 2 sorted arrays requires iterative exclusion
# 2) remember to use rank other then idx, since it is more natual for exclusion
# - comment: this question is very tricky. ultra-hard to finish in 15min if not done before
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def find_kth(k, nums1, nums2):
	    to_exclude = k - 1
            excluded1 = excluded2 = 0
            while to_exclude > 0 and excluded1 != len(nums1) and excluded2 != len(nums2) :
                want_to_exclude = (to_exclude + 1) // 2
                exclude_candid_idx1 = min(excluded1 + want_to_exclude - 1, len(nums1) - 1)
                exclude_candid_idx2 = min(excluded2 + want_to_exclude - 1, len(nums2) - 1)
                cand1 = nums1[exclude_candid_idx1]
                cand2 = nums2[exclude_candid_idx2]
                if cand1 > cand2 :
                    excluded2 = exclude_candid_idx2 + 1 
                else :
                    excluded1 = exclude_candid_idx1 + 1 
                to_exclude = (k - 1) - (excluded1 + excluded2)
            if excluded1 == len(nums1) :
                return nums2[k - len(nums1) - 1]
            elif excluded2 == len(nums2) :
                return nums1[k - len(nums2) - 1]
            else:
                return min(nums1[excluded1], nums2[excluded2])
        total_len = len(nums1) + len(nums2)
        lower_rank = (total_len + 1) // 2
        higher_rank = (total_len + 2) // 2
        return (find_kth(lower_rank, nums1, nums2) + find_kth(higher_rank, nums1, nums2)) / 2.0

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [2, 3, 4, 5]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 3.5
    nums1 = [1, 2, 3]
    nums2 = [4, 5]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 3
    nums1 = [2]
    nums2 = []
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2
    nums1 = []
    nums2 = [2, 3]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5
    nums1 = [3, 4, 5, 6]
    nums2 = [1, 2]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 3.5
    nums1 = [3]
    nums2 = [1, 2, 4]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5

