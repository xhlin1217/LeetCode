# question: what happen if array is empty or it is none?
#       by test leetcode: it it will return null if array is empty
# Logic:
#     same as Binary search but need some additional check for left and right index
#     set left to mid when mid pointer equal to target 
#     after while loop check the following scenarios
#         1. target eqaul to left or right pointer value, return pointer value
#         2. target less than nums[left], return left pointer value
#         3. target greater than nums[right], return right pointer value + 1
#         4. target between nums[left] and nums[right], return right pointer value

class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return none
        left, right, result = 0, len(nums) - 1, None
        while(left + 1 < right):
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                result = mid
                left = mid
                break
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            result = left
        elif nums[right] == target:
            result = right
        elif nums[left] > target:
            result = left
        elif nums[left] < target & target < nums[right]:
            result = right
        else:
            result = right + 1
        return result


obj = Solution()
nums = [1,3,5,6]
target = 3
reuslt = obj.searchInsert(nums, target)
print(reuslt)