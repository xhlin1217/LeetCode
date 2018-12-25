Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

```
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

Logic:
Goal: find a + b + c closest value to the target (a,b,c in nums)

```
Time: O(n^2) + sorting
Space: O(1) + sorting
1. check if num is none or empty array
2. sort nums
3. result, smallest_diff, current_diff = None, None, None
4. loop a_index and a value with in nums
    4.1. b_index, c_index = a_index + 1, size(num) - 1
    while b_index < c_index
        4.2. total = a + b + c using 4.1 index value
        4.3.3. condition
            if total == target
                return target
            elif total < target:
                b_index += 1
            else
                c_index -= 1
            end
        4.3.4. find smallest difference
            current_diff = abs(total - target)
            if smallest_diff is none or smallest_diff > current_diff
                smallest_diff = current_diff
                result = total
return result
```
