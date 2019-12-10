# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not pattern: return not s
        f_match = bool(s) and pattern[0] in {s[0], '.'}
        if len(pattern) > 1 and pattern[1] == '*':
            return (self.match(s, pattern[2:]) or
                    (f_match and self.match(s[1:], pattern)))
        else:
            return f_match and self.match(s[1:], pattern[1:])