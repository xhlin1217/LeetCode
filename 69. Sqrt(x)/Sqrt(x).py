# binary seary logic:
# 2 different way to implement both way are easy
# #1  using binary search template
# #2  using newton methods
#     time: O((log x)^3) - log x
#     space: O(1)

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right, result = 0, x, 1
        while (left + 1 < right):
            mid = left + (right - left) // 2
            mid_sqr = mid ** 2
            if mid_sqr == x:
                return mid
            elif mid_sqr < x:
                left = mid
            else:
                right = mid
        if right ** 2 == x:
            return right
        else:
            return left




class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = x
        while guess ** 2 > x:
            guess = (guess + x // guess) // 2
        return guess

        
obj = Solution()
for x in range(17):
    result = obj.mySqrt(x)  
    print(str(x) + ' -> ' + str(result))