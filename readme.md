Binary Search

![Search in Rotated Sorted Array](Images\BinarySearch\Search&#32;in&#32;Rotated&#32;Sorted&#32;Array.png)
```
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while(left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # elif nums[left] <= target <= nums[mid]:
            #     right = mid
            # else:
            #     left = mid
            elif nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < nums[right]:
                if nums[right] >= target >= nums[mid]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
```