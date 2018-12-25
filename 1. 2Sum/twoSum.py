# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i_index, i in enumerate(nums):
#             for j_index, j in enumerate(nums[i_index+1:]):
#                 if i + j == target:
#                     return [i_index, j_index+i_index + 1]


# obj = Solution()
# nums, targets = [9, 3, 5, 6, 7, 8], 10
# print(obj.twoSum(nums, targets))
# # time: O(n^2)
# # space:O(1)


# class Solution:
#     def twoSum(self, nums, target):
#         nums.sort()
#         l, r = 0, len(nums) - 1
#         while(l < r):
#             if nums[l] + nums[r] == target:
#                 return [l, r]
#             elif nums[l] + nums[r] < target:
#                 l += 1
#             else:
#                 r -= 1


# obj = Solution()
# nums = [1, 4, 2, 3]
# target = 7
# print(obj.twoSum(nums, target))
# # time：O(n)
# # space: O(1)
# # not work in leetcode, since this solution is depends on sort array


# class Solution:
#     def twoSum(self, nums, target):
#         maps = {}
#         for index, num in enumerate(nums):
#             if num not in maps:
#                 maps[num] = index
#             complement = target - num
#             if complement in maps and maps[complement] != index:
#                 return [maps[complement], index]


# obj = Solution()
# nums = [3, 4, 2, 3]
# target = 6
# print(obj.twoSum(nums, target))
# # time：O(n)
# # space: O(n)


# online solution
class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for ind, num in enumerate(nums):
            comp = target-num
            if comp in num_dict:
                return [num_dict[comp], ind]
            else:
                num_dict[num] = ind


obj = Solution()
nums = [3, 4, 2, 3]
target = 6
print(obj.twoSum(nums, target))
# time：O(n)
# space: O(n)
