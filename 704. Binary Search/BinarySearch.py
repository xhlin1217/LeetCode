#%%
# Binary search in any position
# logic:    left and right push to the middle
#           stop when both pointer next to each other
#           last check both pointer, 
#           return if any pointer's value equal to target
# keypoint: 
#           while loop condition (left + 1 < right)
#           mid pointer calculation: left + (right - left) / 2
#    *******convert mid pointer to integer
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right, result = 0, len(nums) - 1, -1
        while(left + 1 < right):
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                result = mid
                break
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            result = left
        elif nums[right] == target:
            result = right
        return result
    

obj = Solution()
nums = [-1,0,3,5,9,12]
target = 2
result = obj.search(nums, target)
print(result)
print(nums[result])