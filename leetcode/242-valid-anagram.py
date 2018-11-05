# https://leetcode.com/problems/valid-anagram/description/


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_len = len(s)
        t_len = len(t)

        if s_len == 0 and t_len == 0:
            return True
        elif s_len != t_len:
            return False
        elif s_len == 1 and t_len == 1:
            return s == t

        s_occurrences = {}
        for char in s:
            if char in s_occurrences:
                s_occurrences[char] += 1
            else:
                s_occurrences[char] = 1

        for char in t:
            if char not in s_occurrences:
                return False
            s_occurrences[char] -= 1
            if s_occurrences[char] < 0:
                return False
        return True


sol = Solution()
res = sol.isAnagram('anagram', 'nagaram')
assert res

# O(s+t)
# 52ms: Very good!! :-) (beats 84% of python submissions)
