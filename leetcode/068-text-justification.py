# https://leetcode.com/problems/text-justification/description/


class Solution(object):
    def fullJustify(self, words, max_width):
        """
        :type words: List[str]
        :type max_width: int
        :rtype: List[str]
        """
        result = []
        curr = []
        curr_char_len = 0
        # 1st to N-1th row
        for word in words:
            word_len = len(word)
            if curr_char_len + len(curr) + word_len > max_width:
                curr_len = len(curr)
                if curr_len == 1:
                    result.append(curr[0] + ' '*(max_width-curr_char_len))
                else:
                    spaces = (max_width - curr_char_len) // (curr_len - 1)
                    extra = (max_width - curr_char_len) % (curr_len - 1)
                    i = 0
                    row = ''
                    for curr_word in curr:
                        row += curr_word
                        if i < curr_len-1:
                            row += ' '*spaces
                        if extra > 0:
                            row += ' '
                            extra -= 1
                        i += 1
                    result.append(row)
                curr.clear()
                curr_char_len = 0
            curr_char_len += word_len
            curr.append(word)
        # Nth row
        i = 0
        row = ''
        for curr_word in curr:
            if i > 0:
                row += ' '
            row += curr_word
            i += 1
        if len(row) < max_width:
            row += ' '*(max_width-len(row))
        result.append(row)
        return result


s = Solution()

j = s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
assert j == [
               "This    is    an",
               "example  of text",
               "justification.  "
            ]

j = s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
assert j == [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
            ]

j = s.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                   "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20)
assert j == [
                  "Science  is  what we",
                  "understand      well",
                  "enough to explain to",
                  "a  computer.  Art is",
                  "everything  else  we",
                  "do                  "
            ]

# 44ms: decent enough, but beats only 23% of python submissions. Would be nice not having to traverse curr every time
# O(2N)? Not sure...
