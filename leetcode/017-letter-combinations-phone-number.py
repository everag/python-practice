# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# DFS (depth first search) solution


class Solution:
    lettermap = {
        '2': [97, 3],
        '3': [100, 3],
        '4': [103, 3],
        '5': [106, 3],
        '6': [109, 3],
        '7': [112, 4],
        '8': [116, 3],
        '9': [119, 4]
    }

    def letterCombinations(self, digits):
        return self.dig(0, digits, '', []) if len(digits) > 0 else []

    def dig(self, index, digits, combo, result):
        digit_info = self.lettermap[digits[index]]
        for charcode in range(digit_info[0], digit_info[0] + digit_info[1]):
            letter = chr(charcode)
            if index+1 == len(digits):
                result.append(combo+letter)
            else:
                self.dig(index+1, digits, combo+letter, result)
        return result


sol = Solution()
res = sol.letterCombinations('23')
print(res)
assert res == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# 52ms = Acceptable but not great... still need improvement!
