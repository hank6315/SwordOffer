# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        num = 0
        for _ in range(32):
            num += n & 1
            n >>= 1
            
        return num