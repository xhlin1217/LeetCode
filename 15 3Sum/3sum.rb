def three_sum(nums)
    result = []
    return result if nums == nil or nums.size == 0
    nums.sort!
    nums.each_with_index do |a, a_index|
        next if a_index >= 1 && nums[a_index-1] == a
        b_index, c_index = a_index + 1, nums.size - 1
        while b_index < c_index
            total = a + nums[b_index] + nums[c_index]
            if total < 0
                b_index += 1
            elsif total > 0
                c_index -= 1
            else
                result << [a, nums[b_index], nums[c_index]]
                while (b_index < c_index && nums[b_index] == nums[b_index + 1])
                    b_index += 1 
                end
                while (b_index < c_index && nums[c_index] == nums[c_index - 1])
                    c_index -= 1 
                end
                b_index += 1
                c_index -= 1
            end
        end
    end
    result
end


nums = [-1, 0, 1, 2, -1, -4]
p three_sum(nums)

# Time: Sorting(ruby sorting algo) + O(n^2)
# space: o(1)