class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) < 3:
            return 0
        nums.sort()
        result, smallest_diff, current_diff = None, None, None
        for a_index in range(len(nums)-2):
            b_index, c_index = a_index + 1, len(nums) - 1
            while b_index < c_index:
                total = nums[a_index] + nums[b_index] + nums[c_index]
                # print(str(a) + ' : ' +
                #       str(nums[b_index]) + ' : ' + str(nums[c_index]) + ' = ' + str(total))
                if total == target:
                    return target
                elif total < target:
                    b_index += 1
                else:
                    c_index -= 1

                current_diff = abs(total - target)
                if smallest_diff == None or smallest_diff > current_diff:
                    smallest_diff = current_diff
                    result = total
        return result


obj = Solution()
nums, target = [-1, 2, 1, -4], 1
print(obj.threeSumClosest(nums, target))
