Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ]

```
Logic: a + b + c = 0
result = []
1. sort array
2. loop one all element in nums
   2.1. skip a if a >= 1 and nums[a_index] == a
   2.2. b_index, c_index = a_index + 1, size of nums - 1
   2.3. while b_index < c_index
        total = a + b + c
        if total == 0
            result = [a, b, c]
            b_index++ till b is different value
            c_index-- till c is different value
        elsif total < 0
            b_index++
        else
            c_index--
```
