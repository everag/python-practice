# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# DFS (depth first search) solution


class Solution:
    lettermap = {
        '2': [ord('a'), 3],
        '3': [ord('d'), 3],
        '4': [ord('g'), 3],
        '5': [ord('j'), 3],
        '6': [ord('m'), 3],
        '7': [ord('p'), 4],
        '8': [ord('t'), 3],
        '9': [ord('w'), 4]
    }

    def letterCombinations(self, digits):
        return self.dig(0, digits, '', []) if len(digits) > 0 else []

    def dig(self, index, digits, combo, result):
        digit_info = self.lettermap[digits[index]]
        for char_code in range(digit_info[0], digit_info[0] + digit_info[1]):
            letter = chr(char_code)
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
