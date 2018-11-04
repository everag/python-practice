# https://leetcode.com/problems/generate-parentheses/description


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.gen('(', 1, result, n)
        return result

    def gen(self, parenthesis, factor, result, n):
        if len(parenthesis) is n*2:
            result.append(parenthesis)
        if factor+1 <= n and parenthesis.count('(') < n:
            self.gen(parenthesis + '(', factor+1, result, n)
        if factor-1 >= 0:
            self.gen(parenthesis + ')', factor-1, result, n)


sol = Solution()
res = sol.generateParenthesis(3)
print(res)
assert set(res) == {"((()))", "(()())", "(())()", "()(())", "()()()"}

# O(2N)
# 72ms - Not so good. I feel counting ( occurrences is not optimal.
# Also, wanna try using bitwise operations: (=1 , )=0
