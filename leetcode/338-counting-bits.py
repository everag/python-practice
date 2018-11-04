# https://leetcode.com/problems/counting-bits/description/


class Attempt1:
    @staticmethod
    def count_bits(num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(0, num+1):
            ones = 0
            power = 0
            while (2**power) <= i:
                if i & (2**power) > 0:
                    ones += 1
                power += 1
            res.append(ones)
        return res


assert Attempt1.count_bits(2) == [0, 1, 1]
assert Attempt1.count_bits(5) == [0, 1, 1, 2, 1, 2]

# 800ms = terrible! need to try again
