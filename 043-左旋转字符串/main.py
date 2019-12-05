# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s :
            return ''
        
        n = n % len(s)
        
        return s[n:] + s[:n]