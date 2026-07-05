def minSubArrayLen(target, nums):
    if not nums:
        return 0
    left, right, current_sum, min_len = 0, 0, 0, float('inf')
    while right < len(nums):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
        right += 1
    return min_len if min_len != float('inf') else 0


'''

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


The outer while loop iterates through all the elements in the array and the inner while loop iterates while current_sum is greater than or equal to the target. Then the minimum length is updated and the left pointer is moved to the right. The right pointer is also moved to the right at the end of each iteration.

This approach has a time complexity of O(n), where n is the length of the input array, as we are iterating through the array twice.

You can test the code with the provided examples:

print(minSubArrayLen(7, [2,3,1,2,4,3]))
# Expected output: 2
print(minSubArrayLen(4, [1,4,4]))
# Expected output: 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
# Expected output: 0

Another approach would be to use binary search, but this will require sorting the array first, and the time complexity would be O(nlogn) since binary search is O(logn) and sorting is O(nlogn).
'''