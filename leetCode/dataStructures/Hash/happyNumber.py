# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
"""  happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy. """

class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()
        stop = False
        reached_1 = False
        while not stop:
            n_str = str(n)
            sum = 0
            for i in n_str:
                sum += int(i)**2
            if (sum == 1):
                stop = True
                reached_1 = True
            if (sum in sum_set):
                stop = True
            else:
                sum_set.add(sum)
                n = sum
        return reached_1

# apparently this was a very slow solution
# although it could be prettier, the logic from faster solutions are pretty much the same, although some are not even using sets, but lists, which seem slower..
# copied from a faster submission:

    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1