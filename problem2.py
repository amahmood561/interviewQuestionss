class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the two sorted arrays
        merged = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        # Add any remaining elements from nums1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        # Add any remaining elements from nums2
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        # Find the median of the merged array
        if len(merged) % 2 == 1:
            median = merged[len(merged) // 2]
        else:
            median = (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
        return median

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''