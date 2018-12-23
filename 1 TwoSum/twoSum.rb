# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    nums.each_with_index do |i, i_index|
        nums[i_index+1..nums.size].each_with_index do |j,j_index|
            if i + j == target
                return [i_index, i_index+j_index+1]
            end
        end
    end
end
nums, target = [0,1,2,3,4,5,6,7,8,9], 10
p two_sum(nums, target)
# time O(n^2)
# space: o(1)


# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    i, j = 0, 0
    while i < nums.size
        j = i + 1
        while j < nums.size
            return [i, j] if nums[i] + nums[j] == target
            j += 1
        end
        i += 1
    end
end
nums =[1,2,3,4,5]
target = 8
p two_sum(nums, target)
time: O(n^2)
space: O(1)



def two_sum(nums, target)
    nums = nums.sort
    l, r = 0, nums.size - 1
    while l < r
        if nums[l] + nums[r] == target
            return [l, r]
        elsif nums[l] + nums[r] < target
            l += 1
        else
            r -= 1
        end
    end
end
nums =[1,2,3,4,5]
target = 8
p two_sum(nums, target)
# time：O(n)
# space: O(1)
# not work in leetcode, since this solution is depends on sort array




def two_sum(nums, target)
    maps = {}
    nums.each_with_index do |num, index|
        maps[num] = index if maps[num] == nil
        complement = target - num
        if maps.has_key?(complement) and maps[complement] != index
            return [maps[complement], index]
        end
    end
end
nums =[3,3]
target = 6
p two_sum(nums, target)
# time: o(n)
# space: O(n)