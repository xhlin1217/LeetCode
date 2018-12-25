class Solution:
    def threeSum(self, nums):
        if nums is None or len(nums) < 3:
            return []
        nums.sort()
        result = []
        for a_ind, a in enumerate(nums):
            if a_ind >= 1 and nums[a_ind - 1] == a:
                continue
            b_ind, c_ind = a_ind + 1, len(nums) - 1
            while b_ind < c_ind:
                total = a + nums[b_ind] + nums[c_ind]
                if total == 0:
                    temp = [a, nums[b_ind], nums[c_ind]]
                    result.append(temp)
                    while b_ind < c_ind and nums[b_ind+1] == nums[b_ind]:
                        b_ind += 1
                    while b_ind < c_ind and nums[c_ind-1] == nums[c_ind]:
                        c_ind -= 1
                    b_ind += 1
                    c_ind -= 1
                elif total < 0:
                    b_ind += 1
                else:
                    c_ind -= 1
        return result


obj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(obj.threeSum(nums))


# Time: Sorting(ruby sorting algo) + O(n^2)
# space: o(1)
