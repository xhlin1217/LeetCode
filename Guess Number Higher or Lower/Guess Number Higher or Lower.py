class Soluction(object):
    def __init__(self, target):
        self.target = target

    def guess(self, num):
        if num == self.target:
            return 0
        elif num < self.target:
            return -1
        else:
            return 1

    def guessNumber(self, n):
        low, high = 1, n
        while(low + 1 < high):
            mid = low + (high - low) // 2
            mid_result = self.guess(mid)
            if mid_result == 0:
                return mid
            elif mid_result == -1:
                low = mid
            else:
                high = mid
        if guess(high) == 0:
            return high
        else:
            return low

target, n = 6, 10
obj = Soluction(target)
print(obj.guessNumber(n))