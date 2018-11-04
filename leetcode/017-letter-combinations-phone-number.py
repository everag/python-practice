# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


class Solution:
    lettermap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits):
        return self.dig(0, digits, '', []) if len(digits) > 0 else []

    def dig(self, index, digits, combo, result):
        for letter in self.lettermap[digits[index]]:
            if index+1 == len(digits):
                result.append(combo+letter)
            else:
                self.dig(index+1, digits, combo+letter, result)
        return result


sol = Solution()
res = sol.letterCombinations('23')
print(res)
assert res == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# 60ms = Acceptable but not great... need to try again
