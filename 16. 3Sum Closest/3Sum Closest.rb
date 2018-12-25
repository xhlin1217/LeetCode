def three_sum_closest(nums, target)
    return 0 if nums == nil || nums.size == 0
    nums.sort!
    result, smallest_diff, current_diff = nil, nil, nil
    (0...nums.size).each do |a_index|
        b_index, c_index = a_index + 1, nums.size - 1
        while b_index < c_index
            total = nums[a_index] + nums[b_index] + nums[c_index]
            if total == target
                return target
            elsif total < target
                b_index += 1
            else 
                c_index -= 1
            end
            current_diff = (total - target).abs
            if smallest_diff == nil or smallest_diff > current_diff
                smallest_diff = current_diff
                result = total
            end
        end
    end
    result
end

nums, target = [-1, 2, 1, -4], 1
print(three_sum_closest(nums, target))