# https://leetcode.com/problems/palindrome-number/description/


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 is 0:
            return False

        original = 0+x
        reverse = 0

        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10

        return reverse == original


assert Solution().isPalindrome(0) is True
assert Solution().isPalindrome(1) is True
assert Solution().isPalindrome(-1) is False
assert Solution().isPalindrome(10) is False
assert Solution().isPalindrome(11) is True
assert Solution().isPalindrome(12) is False
assert Solution().isPalindrome(121) is True
assert Solution().isPalindrome(1001) is True
assert Solution().isPalindrome(12321) is True
assert Solution().isPalindrome(123321) is True
assert Solution().isPalindrome(123221) is False
assert Solution().isPalindrome(1000021) is False
assert Solution().isPalindrome(1000000099) is False  # Overflow case

# 148ms: Very good! beats 79% of python submissions
# I want to try another solution going digit by digit, right to middle and left to middle, comparing the edges.
# I feel it may be more performatic for finding a non-palindromic big number other than reversing the whole thing
